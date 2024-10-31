#!/usr/bin/python

import argparse
import json
import logging
import os
from sys import argv

import requests

URL = "https://api.megatr.ee/api/callback"
DEV_URL = "https://10.10.2.25/api/callback"

script_dir = os.path.dirname(os.path.abspath(argv[0]))

logging.basicConfig(
    filename=script_dir + "/callbacks.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(name)s:%(levelname)s:%(message)s",
)
logging.info("----------")


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", required=False)
parser.add_argument("-l", "--list", action="store_true")
parser.add_argument("-d", "--data")
args = parser.parse_args()

if args.list:
    # Tell the plugin that we should be registered for media
    print("media,playlist")

if args.type:
    data = json.loads(args.data)
    payload = {"type": args.type, "data": data}
    r = requests.post(url=URL, data=payload)
    r = requests.post(url=DEV_URL, data=payload)
    print(payload)
