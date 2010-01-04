import os, platform
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config.ini")


# I intend to hide the Operating Specific details of opening a folder
#   here in this module.  
# 
# On Mac OS X you do this with "open"
#   e.g. "open '\Users\golliher\Documents\Tickler File'"
# On Windows you do this with "explorer"
#   e.g. "explorer c:\Documents and Settings\Tickler File"


def open_folder(path):
    path = os.path.normpath(path)
    cmd = {'Darwin': 'open',      # aka. Mac OS X
           'Linux':  config.get('linux','file_explorer'), 
           'Windows':'explorer'}[platform.system()]
    format_string = {'Darwin': "%s '%s'",  # note the quotation marks around path
                     'Linux':  "%s '%s'", # BUG:  not all Linux distros use nautilus
                     'Windows': "%s %s"}[platform.system()]
    os.popen(format_string % (cmd, path))
    
