#!/bin/bash
set -x

sudo apt-get update && sudo apt-get install -y python3 python3-pip python3-pydantic python3-requests;

echo Restarting FPP...
curl http://localhost/api/system/fppd/restart
echo ...Done
