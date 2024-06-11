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


parser = argparse.ArgumentParser(description="RDS Setting Application")
parser.add_argument(
    "-t", "--type", help="Input station name (8 characters max)", required=False
)
parser.add_argument("-l", "--list", help="Song name", action="store_true")
parser.add_argument("-d", "--data", help="Song name")
args = parser.parse_args()

if args.list:
    # Tell the plugin that we should be registered for media
    print("media,playlist")

if args.type:
    # Look for our type of plugin, doubt this is even needed at all
    logging.debug(args.type)
    # print "My type args: %s" %mytypearg

if args.data and args.media:
    data = json.loads(args.data)
    # title = data["title"]
    # print "Title: %s" %title
    logging.debug(args.data)

if args.data and args.playlist:
    data = json.loads(args.data)
    logging.debug(args.data)
