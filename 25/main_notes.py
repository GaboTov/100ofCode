
""" with open('25/weather_data.csv') as data:
    new_data = data.readlines()

print(new_data) """

""" import csv 
with open('25/weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    #get temperatures
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
    print(temperatures) """

import pandas as pd

#data = pandas.read_csv("25/weather_data.csv")

""" #print (data["temp"])
data_dict = data.to_dict()
print(data_dict)

list_temps= data["temp"].to_list()
avg_list_temps = data["temp"].mean()
print(avg_list_temps) """

#print(data[data.temp == data.temp.max()])

""" data_df= pandas.DataFrame(data)
print(data_df) """

data = pd.read_csv('25/park.csv')

colors = data["Primary Fur Color"]
red_count = len(data[data["Primary Fur Color"] == 'Cinnamon'])
black_count = len(data[data["Primary Fur Color"] == 'Black'])
grey_count = len(data[data["Primary Fur Color"] == 'Gray'])
data_dict = {'Fur Color':['grey','red','black'],
             'Count':[grey_count,red_count,black_count]}

pd.DataFrame(data_dict).to_csv("25/squirrel_count.csv")