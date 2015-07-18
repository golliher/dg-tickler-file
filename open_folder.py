import os, platform
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

    try:
        platform_cmd_formatstring = { 'Darwin':  "open '%s'",  # note the quotation marks around path
                                      'Linux':   "xdg-open '%s'",
                                      'Windows': "explorer %s"}[platform.system()]
    except:
        raise Exception("Your operating system was not recognized.  Unable to determine how to open folders for you.")


    platform_cmd = platform_cmd_formatstring % path

    os.popen(platform_cmd)
