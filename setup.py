#!/usr/bin/env python

import os
from crontab import CronTab

def cron_tab_exists(cron, comment):
    for c in cron.find_comment(comment):
        return True

    return False

def add_cron_entry(dir_name):
    root_cron = CronTab(user='root')

    if cron_tab_exists(root_cron, dir_name):
        print('Cron entry already exists for {0}'.format(dir_name))
        return True

    job = root_cron.new(command=dir_name + '/run', comment=dir_name)

    if -1 != dir_name.find('minute_'):
        minutes = dir_name[dir_name.find('minute_') + len('minute_'):]
        job.minute.every(minutes)
    elif -1 != dir_name.find('hour_'):
        hours = dir_name[dir_name.find('hour_') + len('hour_'):]
        job.hour.every(hours)
    elif -1 != dir_name.find('time_'):
        hour = dir_name[dir_name.find('time_') + len('time_'):]
        job.hour.on(hour)
    else:
        return False

    root_cron.write()
    
    return True

if __name__ == '__main__':
    for dir in [x[0] for x in os.walk('.')]:
        if dir == '.':
            continue
        dir = os.path.abspath(dir)
        if not add_cron_entry(dir):
            print('ERROR: could not add entry for {0}'.format(dir))
