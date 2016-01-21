# nxos

SCRIPT: autoconfig.py

- Script is an enhancement to the GIT/EEM example in Cisco NXOS Programmability and Automation book.
http://www.cisco.com/c/dam/en/us/td/docs/switches/datacenter/nexus9000/sw/open_nxos/programmability/guide/Programmability_Open_NX-OS.pdf . Script runs in N9k guestshell, triggered by an EEM applet running on Nexus 9k. File is then moved to a directory on local git repo in guestshell, then pushed to an external git repo. Do an Internet search to find lots of good info on installing and configuring git     and git server. Couple of notes:
1) You'll see a command in the .py of:  "push". Depending on your implementation of git/server, you might need:  "push origin master" instead.
2) if you run into authentication challengs, check out this link: http://superuser.com/questions/338511/how-do-i-disable-password-prompts-when-doing-git-push-pull



SCRIPT show-mac-interface.py

- Enter and IP Address and output will return : MAC address and interface from which the MAC was learned. Helps in quick troublshooting.



