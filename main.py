#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'
	dir_user = '/home/mint'
else:
	dir_develop='/home/' + uname + '/develop'
	dir_user = '/home/' + uname

# Everything up to this point is common to all Python scripts called by shared-*.sh
# =================================================================================

def add_pkg (packages):
    os.system ('echo INSTALLING ' + packages)
    os.system ('apt-get install -qq ' + packages)

os.system ('echo ===========================')
os.system ('echo BEGIN ADDING CONTROL CENTER')

import shutil, subprocess

add_pkg ('lxrandr') # Add monitor configuration tool
	
src = dir_develop + '/ui-config-general/usr_local_bin/config-general.py'
dest = '/usr/local/bin/config-general.py'
shutil.copyfile (src, dest)
os.system ('chmod a+rx ' + dest)

src = dir_develop + '/ui-config-general/usr_share_applications/config-general.desktop'
dest = '/usr/share/applications/config-general.desktop'
shutil.copyfile (src, dest)

os.system ('echo FINISHED ADDING CONTROL CENTER')
os.system ('echo ==============================')
