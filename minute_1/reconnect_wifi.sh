#!/usr/bin/env bash

if ifconfig wlan0 | grep -q "inet addr:"
then
    date >> cron.log
    echo "Network connection down! Attempting reconnect." >> cron.log
    ifdown wlan0
    sleep 5
    ifup --force wlan0
fi
