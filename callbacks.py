#!/usr/bin/python

import argparse
import json
import logging
import os
from sys import argv

import requests

# BEGIN_URL = "http://192.168.56.211:8000/api/fpp/callback/begin"
# END_URL = "http://192.168.56.211:8000/api/fpp/callback/end"
# STOP_URL = "http://192.168.56.211:8000/api/fpp/callback/stop"

# BEGIN_URL = "http://10.10.2.5:8000/api/fpp/callback/begin"
QUERY_NEXT_URL = "http://10.10.2.5:8000/api/fpp/callback/query_next"
STOP_URL = "http://10.10.2.5:8000/api/fpp/callback/stop"
START_URL = "http://10.10.2.5:8000/api/fpp/callback/start"
PLAYING_URL = "http://10.10.2.5:8000/api/fpp/callback/playing"


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

    if args.type == "playlist":
        action = data.get("Action", "")

        if action == "query_next":
            current_entry = data.get("currentEntry")
            type = current_entry.get("type")
            if type == "media" or type == "both":
                song = current_entry.get("mediaName", "")
                payload = {"song": song}
                r = requests.post(url=QUERY_NEXT_URL, json=payload)

        elif action == "start":
            # action = start AND type = media
            current_entry = data.get("currentEntry")
            type = current_entry.get("type")
            if type == "media" or type == "both":
                song = current_entry.get("mediaName", "")
                size = data.get("size", 0)
                name = data.get("name", "")
                payload = {"song": song, "size": size, "name": name}
                r = requests.post(url=START_URL, json=payload)

        elif action == "playing":
            # action = playing and type = media OR both
            current_entry = data.get("currentEntry")
            type = current_entry.get("type")
            if type == "media" or type == "both":
                song = current_entry.get("mediaName", "")
                payload = {"song": song}
                r = requests.post(url=PLAYING_URL, json=payload)

        elif action == "stop":
            r = requests.get(url=STOP_URL)
