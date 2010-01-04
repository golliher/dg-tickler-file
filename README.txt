Hello,

I wrote this to teach[1] myself python.   It's an implementation of a system for filing things to come back to you in the future. 

The concept is simple.  Every day of the year has a folder.  At the start of each day you pull out the folder for today's date and in it you will find things you thought you'd need today.

This is a digital implementation of such a system.   It was inspired by a collection of AppleScripts for doing much the same thing.   I hope someone will find this useful.   Admittedly, some assembly is required. By that I mean there's no fancy installer or GUI wizard to set it up for you.

Good luck and please let me know if you find it useful.


==Initial Setup==

1) Create a config.ini (see sample_config.ini for a starting point)
2) Run setup_tickler_file.py
3) Schedule daily_tickler.py to run daily (you pick your preferred time, I use 6am)

=How to use it=

Simply find the folder for the date in the future you want sometime to come back to  you.  Drag your files into it.  Simple.   When that date arrives, your daily_tickler.py will run and open the folder for you and you'll be presented with it and its contents.

=A little extra help=

tickler-helper.py makes finding the folder for the date in the future easier.  Run it and it will prompt you for the date and then open that date's folder.   It understands things like "next tuesday" "today" and "tomorrow"  (thanks to the parsedatetime module).

You may want to arrange for it to be easy to run this command.  On my mac I launch it with quicksilver.  On windows I setup a hot key such that control-alt-t launches it.

=Tips=

Rename (or copy) tickler-helper.py to use .pyw extension on windows to avoid console opening with the program.  Same goes for daily_ticker.py

=Requirements=

This program requires parsedatetime and wxpython
* http://code.google.com/p/parsedatetime/
* http://www.wxpython.org/

[1] You've been warned.  There are no doubt bugs.  Maybe it'll delete all your files or call your baby ugly.   There is no warranty expressed on implied.  Use at your own risk.  
