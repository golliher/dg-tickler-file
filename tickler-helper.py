#!/usr/bin/python

import parsedatetime.parsedatetime as pdt
import parsedatetime.parsedatetime_consts as pdc
import sys
import os
import time

# create an instance of Constants class so we can override some of the defaults

c = pdc.Constants()

# create an instance of the Calendar class and pass in our Constants # object instead of letting it create a default

p = pdt.Calendar(c)

user_input = sys.stdin.readlines()

try: 
	# parse "tomorrow" and return the result
	result = p.parse(user_input[0])
	result = time.struct_time(result[0])
	print result.tm_mon, result.tm_mday
		
except:
	print "Could not parse your input.  Sorry"


cmd = "open '/Users/golliher/Documents/Tickler File/%s/%s/%s'" %  (result.tm_year, result.tm_mon, result.tm_mday)

os.system(cmd)