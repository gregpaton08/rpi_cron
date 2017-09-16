# RPi Cron

## Cron setup on raspberry pi

cron README

minute_* is run every * minutes
time_* is run at the hour time of *

* install MTA to log cron output
sudo apt-get install postfix

* logs stored in /var/log/syslog
grep CRON /var/log/syslog
