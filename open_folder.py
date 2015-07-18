import os, platform, subprocess
# I intend to hide the Operating Specific details of opening a folder
#   here in this module.
#
# On Mac OS X you do this with "open"
#   e.g. "open '\Users\golliher\Documents\Tickler File'"
# On Windows you do this with "explorer"
#   e.g. "explorer c:\Documents and Settings\Tickler File"
# On Linux xdg-open is a desktop-independant tool

def open_folder(path):
    '''Runs operating specific command to open a folder.  MacOS, Linux & Windows supported'''

    path = os.path.normpath(path)

    if not os.path.isdir(path):
        raise Exception("Folder does not exist.")

    # Find the operating system command to open a folder
    try:
        platform_cmd = {    'Darwin':  "open",  # note the quotation marks around path
                            'Linux':   "xdg-open",
                            'Windows': "explorer"}[platform.system()]
    except:
        raise Exception("Your operating system was not recognized.  Unable to determine how to open folders for you.")

    # Run the operating system command to open the folder
    try:
         subprocess.check_call([platform_cmd,path])
    except OSError, e:
        raise Exception("Failed attempt executing folder opening command for your OS. \nCMD: %s\nARG: %s\nRESULT: %s\n" % (platform_cmd, path, e.strerror) )
