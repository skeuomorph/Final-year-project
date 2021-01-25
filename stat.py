# Author ~ Markela Zeneli
# Goldsmiths, University of London
########################################

import pandas as pd
import os
import fnmatch
import datetime
import math

race = []
gender = []
outcome = []
age = []
count1 = 0
count2 = 0

#Add CSV columns to respective lists
def all(path):
    global race
    global gender
    global outcome
    global age
    
    df = pd.read_csv(path, sep=',')

    race += df['Officer-defined ethnicity'].tolist()
    gender +=df['Gender'].tolist()
    outcome += df['Outcome'].tolist()
    age += df['Age range'].tolist()

#Iterate over time range of CSVs
month1=12
year1=2017
month2=11
year2=2020

def getDates(month1, year1, month2, year2):

    #Start date
    d = datetime.date(year1,month1,15)

    #Size of each step
    month_delta = datetime.timedelta(days=30)

    #End date
    end_date = datetime.date(year2,month2,15)
    print(end_date)

    #Calculates difference in dates (by metric of .days), and turns into months by dividing by 30 and rounding up
    for i in range(math.ceil(((end_date - d).days)/30)):
        #File paths for months with 1 digit (adds a 0 in front to keep in line with format of file path)
        if (d + i*month_delta).month < 10:
            all('data/'+str((d + i*month_delta).year)+'-0'+str((d + i*month_delta).month)+'/'+str((d + i*month_delta).year)+'-0'+str((d + i*month_delta).month)+'-city-of-london-stop-and-search.csv')
            all('data/'+str((d + i*month_delta).year)+'-0'+str((d + i*month_delta).month)+'/'+str((d + i*month_delta).year)+'-0'+str((d + i*month_delta).month)+'-metropolitan-stop-and-search.csv')
        #File paths for later months(10+)
        else:
            all('data/'+str((d + i*month_delta).year)+'-'+str((d + i*month_delta).month)+'/'+str((d + i*month_delta).year)+'-'+str((d + i*month_delta).month)+'-city-of-london-stop-and-search.csv')
            all('data/'+str((d + i*month_delta).year)+'-'+str((d + i*month_delta).month)+'/'+str((d + i*month_delta).year)+'-'+str((d + i*month_delta).month)+'-metropolitan-stop-and-search.csv')

#Call getDates and populate lists
getDates(month1, year1, month2, year2)

#Stats
for i in range(len(race)):
    if race[i] == "White" and gender[i] == "Male" and (age[i] == "10-17" or age[i] == "18-24"):
        count1+=1
        if outcome[i] == "A no further action disposal"  :
            count2+=1
#"""+geography=fixed for count2"""

stat = count2/count1

print(str(count1) + ',' + str(count2))
print(stat)

#Table of stats 