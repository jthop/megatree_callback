#!/usr/bin/python

import json
import logging
import os
from sys import argv

if len(argv) <= 1:
    print("Usage:")
    print(
        "   --list     | Used by fppd at startup. Used to start up the Si4713_RDS_Updater.py script"
    )
    print(
        "   --reset    | Function by plugin_setup.php to reset the GPIO pin connected to the Si4713"
    )
    print("   --exit     | Function used to shutdown the Si4713_RDS_Updater.py script")
    print(
        "   --type media --data '{...}'    | Used by fppd when a new items starts in a playlist"
    )
    print(
        "   --type playlist --data '{...}' | Used by fppd when a playlist starts or stops"
    )
    print("Note: Running with sudo might be needed for manual execution")
    exit()

script_dir = os.path.dirname(os.path.abspath(argv[0]))

logging.basicConfig(
    filename=script_dir + "/callbacks.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(name)s:%(levelname)s:%(message)s",
)
logging.info("----------")
logging.debug("Arguments %s", argv[1:])


logging.info("Processing %s", argv[1])
if argv[1] == "--list":
    logging.debug("media,playlist")

elif argv[1] == "--reset":
    # Not used by FPPD, but used by plugin_setup.php
    logging.debug("RESET")

elif argv[1] == "--exit":
    # Not used by FPPD, but useful for testing
    logging.debug("EXIT")

elif argv[1] == "--type" and argv[2] == "media":
    logging.info("Type media")

    # TODO: Exception handling for json?
    j = json.loads(argv[4])

    # When default values are sent over fifo, other side more or less ignores them
    media_type = j["type"] if "type" in j else "pause"
    media_title = j["title"] if "title" in j else ""
    media_artist = j["artist"] if "artist" in j else ""
    media_tracknum = str(j["track"]) if "track" in j else "0"
    media_length = str(j["length"]) if "length" in j else "0"

    logging.debug("Type is %s", media_type)
    logging.debug("Title is %s", media_title)
    logging.debug("Artist is %s", media_artist)
    logging.debug("Track # is %s", media_tracknum)
    logging.debug("Length is %s", media_length)

    if media_type == "pause" or media_type == "event":
        # blank title, blank artist
        pass
    else:
        # print(media_title)
        # print(media_artist)
        pass
    # TODO: Will tracknum and length never show up at the wrong time?
    # print(media_tracknum)
    # print(media_length)


elif argv[1] == "--type" and argv[2] == "playlist":
    logging.info("Type playlist")

    # TODO: Exception handling for json?
    j = json.loads(argv[4])

    playlist_action = j["Action"] if "Action" in j else "stop"

    logging.info("Playlist action %s", j["Action"])

    if playlist_action == "start":  # or playlist_action == 'playing':
        pass
    elif playlist_action == "stop":
        pass
logging.debug("Processing done")
