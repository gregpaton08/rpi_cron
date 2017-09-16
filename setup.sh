#!/usr/bin/env bash

function addCronTab {
    crontab -l | grep -q -F "$1"
    if [ $? != 0 ]
    then
        (crontab -l 2>/dev/null; echo "$1") | crontab -
    fi
}

if [[ $EUID -ne 0 ]];
then
   echo "This script must be run as root" 1>&2
   exit 1
fi

addCronTab "0 4 * * *  ~/cron/time_4am/run"
