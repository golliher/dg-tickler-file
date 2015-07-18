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

    format_string = {'Darwin': "open '%s'",  # note the quotation marks around path
                     'Linux':  "xdg-open '%s'",
                     'Windows': "explorer %s"}[platform.system()]

    os.popen(format_string % path)
