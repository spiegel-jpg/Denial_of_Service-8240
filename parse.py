# Month wise data for each date for specified year

import argparse
from matplotlib import dates
import matplotlib.pyplot as plt
import re

# Line 10 to 13 - to let the scipt take arguments. 
# You will have to add an argument for day. 

parser = argparse.ArgumentParser(description='Requests.')
parser.add_argument('-d', metavar = 'DAY', dest='DAY', help='Specify the day for which you need the data')
parser.add_argument('-m', metavar = 'MONTH', dest='MONTH' ,help='Specify the month for which you need the data')
parser.add_argument('-y', metavar='YEAR', dest='YEAR', help='Specify the year for which you need the data')
args = parser.parse_args()

day_specified = (args.DAY is not None)


calcDict = {}  # Empty dictionary to hold data
myfile = open("get.log")
for line in myfile:
    pattern = re.compile(r'\[') # Finding the first occurence of '[' using regex to cover all corner cases. 
    matches = pattern.finditer(line)
    for match in matches:
        a = match.span() # this returns a tuple of the index for the above occurence.
        data_year = line[a[1]+7:a[1]+11] # getting the year in the data
        data_month = line[a[1]+3:a[1]+6] # getting the month in the data
        if day_specified :               # if day parameter was provided
            data_day = line[a[1]:a[1]+2] # getting the day in the data ~
        
        # if day parameter not given, collect matching Month/Year
        if args.MONTH == data_month and int(args.YEAR) == int(data_year) and day_specified == False:
            b = line[a[1]:a[1]+2] # Getting date
            if b in calcDict.keys():  
                value = calcDict.get(b)
                calcDict[b] = value + 1
            else:
                calcDict.update({b:1})

        # if day parameter given, collect matching Day's hourly requests
        elif args.MONTH == data_month and int(args.YEAR) == int(data_year) and int(args.DAY) == int(data_day):
            b = line[a[1]+12:a[1]+14] # Getting hour
            if b in calcDict.keys():  
                value = calcDict.get(b)
                calcDict[b] = value + 1
            else:
                calcDict.update({b:1})
names = list(calcDict.keys()) # getting keys from dictionary. 
values = list(calcDict.values()) # getting value from dictionary.

plt.bar(range(len(calcDict)), values, tick_label=names)  # Line 35 to 39 for plotting.
if day_specified == False:      # if plotting for Month
    plt.title("No. of requests for each day in a Month")
    plt.xlabel(args.MONTH + " for the year " + args.YEAR)
else:                           # else plotting for Day
    plt.title("No. of requests for given Day by hour")
    plt.xlabel(args.MONTH + " " + args.DAY + " for the year " + args.YEAR)
plt.ylabel("No. of requests")
plt.show()
