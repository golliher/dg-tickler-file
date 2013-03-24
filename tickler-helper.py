#!/usr/bin/env python
#
# Program that make is easy for user to pop open a folder for a specific date.
#   exampleS:   "next tuesday"  or "20 days"  or "1/1/2011"
#
# I launch this program from Quicksilver.  You could also launch it from Spotlight.
#   I also rename it to th.command for convenience.
import parsedatetime.parsedatetime as pdt
import parsedatetime.parsedatetime_consts as pdc
import sys,os,time
import ConfigParser
from open_folder import open_folder

config = ConfigParser.ConfigParser()
config.read("config.ini")

# create an instance of Constants class so we can override some of the defaults
c = pdc.Constants()

# create an instance of the Calendar class and pass in our Constants 
# object instead of letting it create a default
p = pdt.Calendar(c)

    
if len(sys.argv) >= 2:
    # wx.MessageBox("CLI INPUT DETECTED %s" % sys.argv[1])
    user_input = sys.argv[1]
        
else:
    try:
        import wx
        app = wx.App()
    except:
        print "Unless you specify arguments on the command line wxpython is required."
        print "wxpython not able to be imported. exiting."
        sys.exit(1)

    dlg = wx.TextEntryDialog(None, 'What date should this tickle?','', 'tomorrow')
    if dlg.ShowModal() == wx.ID_OK:
        user_input = dlg.GetValue()
    dlg.Destroy()
    
try: 
    # parse "tomorrow" and return the result as a tuple
    result = p.parse(user_input)
    if result[1] == 0:
         raise Exception("Not able to parse user input")

    result = time.struct_time(result[0])
    folder_name = '{0}/{1}/{2:02}/{3:02}'.format(
                                        config.get("global","tickle_file_dir"),
                                        result.tm_year, 
                                        result.tm_mon, 
                                        result.tm_mday)
    open_folder(folder_name)
    
except:
    wx.MessageBox('Didn\'t understand what you meant by "%s"' 
                                        % user_input,'Sorry...')

if 'app' in globals():
    app.MainLoop()


