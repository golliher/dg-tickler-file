#!/usr/bin/python
#
# Designed to be run daily and pop open today's ticker folder
#  also creates a symlink so that it's easy for user to open "today"
#  if she closes it and wants to open it again
#
import sys,os,time,wx
import time,datetime
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config.ini")

today = datetime.date.today()

# Create string representing the file path to ticker folder for todays date
todays_folder = config.get("global","tickle_file_dir") + "/" + today.strftime("%Y/%m/%d")

the_today_folder = config.get("global","the_today_folder")

# Get rid of the old symlink first
try:
    cmd = 'rm %s' % the_today_folder
    os.system(cmd)
except:
    print("Warning: Unabled to remove old symlink ({1}).".format(the_today_folder))

# Create a symlink to make it easy for user to open up "today"
cmd = 'ln -s "%s" "%s"' % (todays_folder,the_today_folder)
os.system(cmd)

# Go ahead and pop open the folder to it's front and center
cmd = 'open "%s"' % the_today_folder
os.system(cmd)