#!/usr/bin/python
#
#  Creates the folder heiracy of tickler files.   Intended to be run once as
#    part of system setup.  Will need to be run again in a few years when the tickler
#    file is exhausted.
#
# TODO: Make this system self-aware.  Create more years when we run out.
# TODO: Remind user they may want to prune old years.
#
import os,ConfigParser,datetime
config = ConfigParser.ConfigParser()
config.read("config.ini")


day_in_month        = 30
months_in_year      = 12
num_years_to_create = 3 

starting_year = datetime.datetime.today().year
ending_year = starting_year + num_years_to_create

for year in range(starting_year,ending_year+1):
    print year
    for month in range(1,13):
        print "\t%s" % month
        for day in range(1,32):
            print "\t\t%s" % day
            cmd = 'mkdir -p "%s' %  (config.get("global","tickle_file_dir") 
                                        + "/" + str(year) 
                                        + "/" + str(month).zfill(2) 
                                        + "/" + str(day).zfill(2) 
                                        + '"')
            os.system(cmd)