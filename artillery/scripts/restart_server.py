#!/usr/bin/env python
"""
    Restart Artillery
"""

from __future__ import print_function
import os
import subprocess

from artillery.core import kill_artillery
from artillery.core import grab_time
from artillery.core import write_log

proc = subprocess.Popen("ps -A x | grep artiller[y]", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
# kill running instance of artillery
kill_artillery()

print("[*] %s: Restarting Artillery Server..." % grab_time())
if os.path.isfile("/var/artillery/artillery.py"):
    write_log("[*] %s: Restarting the Artillery Server process..." % (grab_time()))
    subprocess.Popen("python /var/artillery/artillery.py &", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
