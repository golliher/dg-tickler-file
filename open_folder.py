import os, platform

# I intend to hide the Operating Specific details of opening a folder
#   here in this module.  
# 
# On Mac OS X you do this with "open"
#   e.g. "open \Users\golliher\Documents\Tickler File"
# On Windows you do this with "explorer"
#   e.g. "explorer c:\Documents and Settings\Tickler File"

# TODO: What operating system are we on?
# Set variable for the commands

def open_folder(path):
    cmd = {'Darwin': 'open',      # aka. Mac OS X
           'Windows':'explorer'}[platform.system()]
    print cmd
    os.system("%s '%s'" % (cmd, path))
    