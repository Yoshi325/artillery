#!/usr/bin/python
#
# monitor apache
#
import time,re, thread
from src.core import *

monitor_frequency = int(read_config("MONITOR_FREQUENCY"))
apache_attempts = read_config("APACHE_BRUTE_ATTEMPTS")


def tail(some_file):
    this_file = open(some_file)
    # Go to the end of the file
    this_file.seek(0,2)

    while True:
        line = this_file.readline()
        if line:
            yield line
        yield None

access = read_config("ACCESS_LOG")
# grab the access logs and tail them
access = "/var/log/apache2/access.log"
access_log = tail(access)

# grab the error logs and tail them
errors = "/var/log/apache2/error.log"
error_log = tail(errors)

def apache_monitor(monitor_frequency):
    #127.0.0.1 - - [10/Mar/2012:15:35:53 -0500] "GET /sdfsdfds.dsfds HTTP/1.1" 404 501 "-" "Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0.2) Gecko/20100101 Firefox/10.0.2"
    
    access = read_config("ACCESS_LOG")
    if (not access):
        access = read_config("APACHE_ACCESS_LOG")
    if (access):
        # determine if it is a dict or string
    
    error = read_config("ERROR_LOG")
    if (not error):
        error = read_config("APACHE_ERROR_LOG")
    if (error):
        # determine if it is a dict or a string
        apache_hammering = read_config("APACHE_ACCESS_LOG")
    # behaviors to look for:
    #   hammering (DDoS)
    #   brute force login (possibly repetitive POST to *login.php)
    #   accessing files that should never be accessed
    #   accessing files too often (access per s)
    apache_hammering = read_config("APACHE_HAMMER_FREQUENCY")
    apache_never = read_config("APACHE_NEVER_LIST")
    apache_access_frequency = read_config("APACHE_ACCESS_FREQUENCY")
    


if is_posix():
    thread.start_new_thread(apache_monitor,(monitor_frequency,))