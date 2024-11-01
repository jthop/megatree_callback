#!/usr/bin/python

import argparse
import json
import logging
import os
from sys import argv

import requests
from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

URL = "https://api.megatr.ee/api/fpp/callback"
DEV_MEDIA_URL = "http://10.10.2.5:8000/api/fpp/callback/media"
DEV_PLAYLIST_URL = "http://10.10.2.5:8000/api/fpp/callback/playlist"

BEGIN_URL = "http://10.10.2.5:8000/api/fpp/callback/begin"
END_URL = "http://10.10.2.5:8000/api/fpp/callback/end"


class ParentModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        extra="ignore",
        alias_generator=to_camel,
    )


class CurrentEntry(ParentModel):
    duration: float | None = None
    enabled: int
    is_finished: int
    is_playing: int
    is_started: int
    media_filename: str | None = None
    media_name: str | None = None
    playCount: int
    play_once: int
    timecode: str | None = None
    type: str


class PlaylistType(ParentModel):
    Action: str
    Item: int
    Section: str
    current_state: str
    loop: int
    loop_count: int
    name: str
    random: int
    repeat: int
    size: int
    current_entry: CurrentEntry | None = None


script_dir = os.path.dirname(os.path.abspath(argv[0]))
logging.basicConfig(
    filename=script_dir + "/callbacks.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(name)s:%(levelname)s:%(message)s",
)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", required=False)
parser.add_argument("-l", "--list", action="store_true")
parser.add_argument("-d", "--data")
args = parser.parse_args()

if args.list:
    # Tell the plugin that we should be registered for media
    print("media,playlist")

if args.type:
    data = PlaylistType.model_validate_json(args.data)
    logging.debug("Wow")
    logging.debug(data)

    if args.type == "playlist":
        logging.info("playlist")
        if data.Action == "query_next" and data.type == "media":
            song = data.current_entry.media_filename
            payload = {song: song}
            r = requests.post(url=END_URL, json=payload)

        elif data.Action == "playing" and data.type == "media":
            song = data.current_entry.media_filename
            duration = data.current_entry.duration
            payload = {song: song, duration: duration}
            r = requests.post(url=BEGIN_URL, json=payload)
