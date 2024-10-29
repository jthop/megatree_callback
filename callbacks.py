#!/usr/bin/python

import argparse
import json
import logging
import os
from sys import argv

script_dir = os.path.dirname(os.path.abspath(argv[0]))

logging.basicConfig(
    filename=script_dir + "/callbacks.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(name)s:%(levelname)s:%(message)s",
)
logging.info("----------")
logging.debug("Arguments %s", argv[1:])


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

    if args.type == "media":
        logging.debug(f"MEDIA - {data}")
    elif args.type == "playlist":
        logging.debug(f"PLAYLIST - {data}")
