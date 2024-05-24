#!/usr/bin/python

import argparse
import json
import logging
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


logging.basicConfig(
    filename="/callbacks.log",
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
    logging.debug(args.list)

if args.type:
    # Look for our type of plugin, doubt this is even needed at all
    logging.debug(args.type)
    # print "My type args: %s" %mytypearg

if args.data:
    # get the json string from FPP
    mydataarg = args.data
    data = json.loads(mydataarg)
    title = data["title"]
    #   print "Title: %s" %title
    logging.debug(args.data)
