#!/usr/bin/python

import argparse
import json
import logging
import os
from sys import argv

import requests

BEGIN_URL = "http://10.10.2.5:8000/api/fpp/callback/begin"
END_URL = "http://10.10.2.5:8000/api/fpp/callback/end"
STOP_URL = "http://10.10.2.5:8000/api/fpp/callback/stop"


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

if args.type and args.data:
    data = json.loads(args.data)
    logging.debug(data)

    if args.type == "playlist":
        action = data.get("Action", "")

        if action == "query_next":
            current_entry = data.get("currentEntry")
            if current_entry.get("type", "") == "media":
                song = current_entry.get("mediaFilename", "")
                payload = {"song": song}
                r = requests.post(url=END_URL, json=payload)

        elif action == "playing" or action == "start":
            current_entry = data.get("currentEntry")
            type = current_entry.get("type")
            if type == "media":
                song = current_entry.get("mediaName", "")
                duration = current_entry.get("duration")
            elif type == "both":
                song = current_entry.get("mediaName", "")
                media = current_entry.get("media", {})
                duration = media.get("secondsRemaining")

            payload = {"song": song, "duration": duration}
            r = requests.post(url=BEGIN_URL, json=payload)

        elif action == "stop":
            r = requests.get(url=STOP_URL)
