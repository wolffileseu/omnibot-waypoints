#!/bin/sh 
#
# IRATA [*] 2010 - use at own risk!
#
# This update script keeps your configs ...
#
# Install svn on target box if not already installed.
# Put this file into your omni-bot path and grant exec permissions.
# Create an additional folder 'backup' in omni-bot path and
# copy your modified omni-bot.cfg, et_botnames.gm and et_autoexec.gm
# into it.
#
# Change shell directory to omni-bot path (important!)
# and call ./botupdate.sh 
#
# There is a limit using this: Keep an eye on et_botnames.gm
# and et_autoexec.gm. If there are changes you need to adjust
# these files in your backup folder.
# New default entries for omni-bot.cfg will be added by OB if used
# and SaveConfigChanges is set to 1.  

# TODO:
# Use a var to set the root URL of target repository for repURL1,2,3
# Optimize: svn export vs. checkout: 
#   this script downloads all again and again ... on the other side export grants us a real copy of the rep 
# if checkout is used delete all .svn files in path ....

user=''
password=''

repURL1='http://svn.assembla.com/svn/omnibot/Enemy-Territory/0.8/omnibot_et.so'
repURL2='http://svn.assembla.com/svn/omnibot/Enemy-Territory/0.8/et/'
repURL3='http://svn.assembla.com/svn/omnibot/Enemy-Territory/0.8/global_scripts'

quiet='--quiet'

#----------------------------------------------------------------------

backupPath='./backup/'

botConfigFile='omni-bot.cfg'
botNamesFile='et_botnames.gm'
botAutoexecFile='et_autoexec.gm'

echo "Getting new rep version ..."

echo "Updating botlib .."
svn export $repURL1 --force --username $user --password $password $quiet
echo "Updating ET scripts .."
svn export $repURL2 --force --username $user --password $password $quiet
echo "Updating global scripts .."
svn export $repURL3 --force --username $user --password $password $quiet

echo "Customizing"
cp $backupPath$botConfigFile ./et/user
cp $backupPath$botNamesFile ./et/scripts
cp $backupPath$botAutoexecFile ./et/scripts

echo "... done."
