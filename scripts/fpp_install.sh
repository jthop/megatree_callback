#!/bin/bash


echo Restarting FPP...
curl http://localhost/api/system/fppd/restart
echo ...Done
