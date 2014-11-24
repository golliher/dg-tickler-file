#!/usr/bin/env python#
# Designed to be run daily and pop open today's ticker folder
#  also creates a symlink so that it's easy for user to open "today"
#  if she closes it and wants to open it again
#
import sys,os,time
import os.path
import time,datetime
import ConfigParser
from open_folder import *

import gntp.notifier

#image = open('./folder-icon-512x512.png', 'rb').read()
image = open('./myfolder.png', 'rb').read()

# More complete example
growl = gntp.notifier.GrowlNotifier(
    applicationName = "Tickler File",
    notifications = ["New Updates","New Messages"],
    defaultNotifications = ["New Messages"],
)
growl.register()



config = ConfigParser.ConfigParser()
config.read("config.ini")

today = datetime.date.today()

# Create string representing the file path to ticker folder for todays date
todays_folder = config.get("global","tickle_file_dir") + "/" + today.strftime("%Y/%m/%d")


    

the_today_folder = config.get("global","the_today_folder")

# Get rid of the old symlink first
try:
    os.remove(the_today_folder)
except:
    print("Warning: Unabled to remove old symlink.")

# Create a symlink to make it easy for user to open up "today"
# (NOTE TO SELF: Perhaps windows users just don't get this convenience? 
#   (because no symlinks on windows)
cmd = 'ln -s "%s" "%s"' % (todays_folder,the_today_folder)
try:
    os.system(cmd)
except:
    print "Failed to create a symlink for today.   This is probably OK."


file_count = len( [name for name in os.listdir(todays_folder) ]   )

if (file_count == 0):
    msg = "Today's tickler file was not opened because it contained no files. \n\n%s" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    growl.notify(
        noteType = "New Messages",
        title = "Checked today's ticker file.",
        description = msg,
        # icon = "http://www.graphicsfuel.com/wp-content/uploads/2012/03/folder-icon-512x512.png",
        # icon = "http://www.theofficedealer.com/mm5/graphics/product_images/1300/seo/Pendaflex-9200T-1-3-Pressboard-File-Folder.jpg",
        icon = image,

        sticky = True,
        priority = 1,
    )
else:
    # Go ahead and pop open the folder to it's front and center
    open_folder(todays_folder)
