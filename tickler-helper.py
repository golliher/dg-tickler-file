#!/usr/bin/python

import parsedatetime.parsedatetime as pdt
import parsedatetime.parsedatetime_consts as pdc
import sys,os,time,wx
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("config.ini")

# create an instance of Constants class so we can override some of the defaults
c = pdc.Constants()

# create an instance of the Calendar class and pass in our Constants 
# object instead of letting it create a default
p = pdt.Calendar(c)

app = wx.App()
dlg = wx.TextEntryDialog(
        None, 'What date should this tickle?',
        '', 'tomorrow')

if dlg.ShowModal() == wx.ID_OK:
    user_input = dlg.GetValue()
    try: 
        # parse "tomorrow" and return the result as a tuple
        result = p.parse(user_input)
        if result[1] == 0:
             raise Exception("Not able to parse user input")

        result = time.struct_time(result[0])
        cmd = "open '%s/%s/%s/%s'" %  (config.get("global","tickle_file_dir"),result.tm_year, result.tm_mon, result.tm_mday)
        os.system(cmd)
    except:
        wx.MessageBox('Didn\'t understand what you meant by "%s"' % user_input,'Sorry...')

dlg.Destroy()
app.MainLoop()

