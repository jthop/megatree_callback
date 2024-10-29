"""
Alternative option was to use unique file ID binary field.
ufid = song.tag.unique_file_ids.get("MD5")
ufid.owner_id="MD5", ufid.uniq_id=hash
iterate via:
for frame in song.tag.unique_file_ids:
    frame.owner_id, frame.uniq_id

also another option to iterate text_frames:
for frame in song.tag.frameiter(["TXXX"]):
"""

import datetime
import glob
import hashlib
import json

import eyed3

MP3_DIR = "/Users/jhopper/Dropbox/lights/xlights/brynmawr/_SHOW/music/"
SHOW_VERSION = "1.0.2"
SHOW_NAME = "Hopper Light Show"
SHOW_GEO_PT = [32.856300, -96.777779]
SHOW_HOURS = "6:00pm to 11:00pm"


def dict_hash(d):
    """MD5 hash of a dictionary."""
    result = hashlib.md5()
    encoded = json.dumps(d, sort_keys=True).encode()
    result.update(encoded)

    return result.hexdigest()


playlist = {}

for file in glob.glob(f"{MP3_DIR}*.mp3", root_dir=MP3_DIR):
    file_name = file.split("/")[-1]
    file_id = file_name.replace(".", "_")
    song = eyed3.load(file)

    # image.picture_type 3=front cover, 4=back, 0=other
    if song.tag.images[0].picture_type == 3:
        album_art = f"{file_id}.jpg"
        image_file = open(f"{MP3_DIR}/images/{album_art}", "wb")
        image_file.write(song.tag.images[0].image_data)
        image_file.close()

    # spotify / youtube link
    link = ""
    spotify_frame = song.tag.user_text_frames.get("SPOTIFY")
    if spotify_frame:
        spotify_id = spotify_frame.text
        link = f"https://open.spotify.com/track/{spotify_id}"
    youtube_frame = song.tag.user_text_frames.get("YOUTUBE")
    if youtube_frame:
        youtube_id = youtube_frame.text
        link = f"https://www.youtube.com/watch?v={youtube_id}"

    playlist[file_name] = {
        "id": file_id,
        "title": song.tag.title,
        "artist": song.tag.artist,
        "album": song.tag.album,
        "year": str(song.tag.getBestDate()),
        "duration": song.info.time_secs,
        "link": link,
        "albumArt": album_art
    }

showSeconds = sum(song["duration"] for song in playlist.values())
db = {
    "name": SHOW_NAME,
    "revision": dict_hash(playlist),
    "version": SHOW_VERSION,
    "location": SHOW_GEO_PT,
    "hours": SHOW_HOURS,
    "totalSeconds": showSeconds,
    "lengthISO": str(datetime.timedelta(seconds=showSeconds)),
    "playlist": playlist,
}


with open('show.json', 'w', encoding='utf-8') as f:
    json.dump(db, f, ensure_ascii=False, indent=4)
