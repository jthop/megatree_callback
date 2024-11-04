#!/usr/bin/python

import argparse
import json
import logging
import os
from sys import argv

import requests

URL = "https://api.megatr.ee/api/fpp/callback"
DEV_MEDIA_URL = "http://10.10.2.5:8000/api/fpp/callback/media"
DEV_PLAYLIST_URL = "http://10.10.2.5:8000/api/fpp/callback/playlist"

BEGIN_URL = "http://10.10.2.5:8000/api/fpp/callback/begin"
END_URL = "http://10.10.2.5:8000/api/fpp/callback/end"


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

logging.debug(args.data)
if args.type and args.data:
    data = json.loads(args.data)

    # logging.debug(data)

    if args.type == "playlist":
        if data.get("Action", "") == "query_next":

            if data.get("currentEntry", {}).get("type", "") == "media":
                song = data.get("currentEntry", {}).get("mediaFilename", "")
                payload = {"song": song}
                r = requests.post(url=END_URL, json=payload)

        elif data.get("Action", "") == "playing" or data.get("Action", "") == "start":

            if data.get("currentEntry", {}).get("type", "") == "media":
                song = data.get("currentEntry", {}).get("mediaFilename", "")
                duration = data.get("currentEntry", {}).get("duration", "")
                payload = {"song": song, "duration": duration}
                r = requests.post(url=BEGIN_URL, json=payload)
