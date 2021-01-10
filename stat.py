import pandas as pd

race = []
gender = []
outcome = []
age = []
count1 = 0
count2 = 0

#add CSV columns to respective lists
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

all('data/2020-03/2020-03-city-of-london-stop-and-search.csv')

all('data/2020-03/2020-03-city-of-london-stop-and-search.csv')

all('data/2020-04/2020-04-metropolitan-stop-and-search.csv')

all('data/2020-04/2020-04-city-of-london-stop-and-search.csv')

all('data/2020-05/2020-05-metropolitan-stop-and-search.csv')

all('data/2020-05/2020-05-city-of-london-stop-and-search.csv')

for i in range(len(race)):
    if race[i] == "Black" and gender[i] == "Male" and (age[i] == "10-17" or age[i] == "18-24"):
        count1+=1
        if outcome[i] == "A no further action disposal" :
            count2+=1

stat = count2/count1

print(str(count1) + ',' + str(count2))
print(stat)