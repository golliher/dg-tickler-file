#!/usr/bin/python

import os,ConfigParser,datetime
config = ConfigParser.ConfigParser()
config.read("config.ini")


day_in_month = 30
months_in_year =12
num_years_to_create = 3 


# TODO: Figure out what year it is right now as of when we are running
today = datetime.date.today()
starting_year = today.year
ending_year = starting_year + num_years_to_create


for year in range(starting_year,ending_year+1):
    print year
    for month in range(1,13):
        print "\t%s" % month
        for day in range(1,32):
            print "\t\t%s" % day
            cmd = 'mkdir -p "%s' %  (config.get("global","tickle_file_dir") 
                                        + "/" + str(year) 
                                        + "/" + str(month) 
                                        + "/" + str(day) 
                                        + '"')
            os.system(cmd)