#!/usr/bin/env bash

#dir="/media/RPI_BACKUP/backup/home"
dir="/mnt/usbdrive/backup/home"

rsync --modify-window=1 -avs /home/ $dir
