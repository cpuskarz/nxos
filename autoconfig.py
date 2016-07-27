#!/usr/bin/python

import os
import subprocess
from subprocess import call

# cpuskarz 11/25/2015 autoconfig.py v1
# Program is an enhancement to EEM/GIT example in the Cisco NX-OS Programmability Guide.
# Program is triggered from EEM script on N9k via copy running-config startup-config
# Moves the output file to a directory on local GIT repo (in guestshell)
# Git adds and commits the file then pushes to a remote GIT repo

# Read running-counter file
fh1 = open("runningcounter.txt", "r")
countset = fh1.read()
fh1.close()

# Reopen running-counter file and write incremental counter
fh2 = open("runningcounter.txt", "w")
inp_count = int(countset) + 1
set_count = str(inp_count)
fh2.write(set_count)
fh2.close()
set_message = "Changed configuration, version: %s" % set_count

# Create file for  output or errors
f = open("autoouptput.txt", "w")
os.chdir("/home/guestshell/autoconfig2.git")

call(["mv", "/bootflash/autoconfig/running.latest", "/home/guestshell/autoconfig2.git/n9k1/running"])
call(["git", "add", "n9k1/running"])
call(['git', 'commit', '-m', set_message])

p = subprocess.Popen(['chvrf', 'management', 'git', 'push origin master'],  stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = p.communicate()
f.write(out)
f.write(err)
f.close()

