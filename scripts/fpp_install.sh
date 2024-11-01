#!/bin/bash
set -x

sudo apt-get update && sudo apt-get install -y python3 python3-pip;
python3 -m pip install requests --break-system-packages;

echo Restarting FPP...
curl http://localhost/api/system/fppd/restart
echo ...Done
