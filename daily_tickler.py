#!/usr/bin/python
import sys,os,time,wx
import ConfigParser
import time,datetime

config = ConfigParser.ConfigParser()
config.read("config.ini")

today = datetime.date.today()

# Create string representing the file path to today's ticker folder
todays_folder = config.get("global","tickle_file_dir") + "/" + today.strftime("%Y/%m/%d")
print todays_folder


# TODO: Create an alias from the tickler folder for today to an alias called simply "Today"
# Maybe there's a better way, but I'll just shell out to "ln -s" and create a symbolic link
the_today_folder = config.get("global","the_today_folder")
cmd = 'ln -s "%s" "%s"' % (todays_folder,the_today_folder)
print cmd
os.system(cmd)

# TODO: Open the today folder so it gets noticed
cmd = 'open "%s"' % the_today_folder
print cmd
os.system(cmd)
