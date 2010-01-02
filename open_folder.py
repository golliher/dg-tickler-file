import os, platform

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
           'Windows':'explorer'}[platform.system()]
    format_string = {'Darwin': "%s '%s'",  # note the quotation marks around path
                     'Windows': "%s %s"}[platform.system()]
    print cmd
    print path
    os.system(format_string % (cmd, path))
    
