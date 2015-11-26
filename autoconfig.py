#!/usr/bin/python

####################################################################################
# Licensed under the Apache License, Version 2.0 (the "License");                  #
# you may not use this file except in compliance with the License.                 #
# You may obtain a copy of the License at                                          #
#                                                                                  #
#     http://www.apache.org/licenses/LICENSE-2.0                                   #
#                                                                                  #
# Unless required by applicable law or agreed to in writing, software              #
# distributed under the License is distributed on an "AS IS" BASIS,                #
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.         #
# See the License for the specific language governing permissions and              #
# limitations under the License.                                                   #
####################################################################################
#                                                                                  #
####################################################################################
# cpuskarz 11/25/2015 - autoconfig.py v1                                           #
# Program is an enhancement to EEM/GIT example in the Cisco NX-OS Programmability  #
# and Automation book. Program is triggered from EEM script on N9k -  copy         #
# running-config startup-config; moves the output file to a directory on local     #
# GIT repo; Git adds and commits the file, then pushes to a remote GIT repo.       #
####################################################################################


import os
import subprocess
from subprocess import call

# Read running-counter file. File needs to pre-created for a starting vpoint.
# Starting version number is arbitrary.
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

# Create file for output and errors. Set up directory structure as needed.
f = open("autoouptput.txt", "w")
os.chdir("/home/guestshell/autoconfig")

call(["mv", "/bootflash/autoconfig/running.latest", "/home/guestshell/autoconfig/n9k1/running"])
call(["git", "add", "n9k1/running"])
call(['git', 'commit', '-m', set_message])

p = subprocess.Popen(['chvrf', 'management', 'git', 'push'],  stdout=subprocess.PIPE, stderr=subprocess.PIPE)

out, err = p.communicate()
f.write(out)
f.write(err)
f.close()
