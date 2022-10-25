import csv
from curses.ascii import isdigit
emmisions_file = open('SYB65_310_202209_Carbon Dioxide Emission Estimates.csv')
data_read = csv.reader(emmisions_file)
emissions_dictionary = list(data_read)

emissions_china = []
emissions_us = []
emissions_years = []
for i in range(len(emissions_dictionary)):
    if emissions_dictionary[i][1] == 'China' and emissions_dictionary[i][3] == 'Emissions per capita (metric tons of carbon dioxide)' :
        emissions_china.append(emissions_dictionary[i][4])
        emissions_years.append(emissions_dictionary[i][2])
    elif emissions_dictionary[i][1] == 'United States of America' and emissions_dictionary[i][3] == 'Emissions per capita (metric tons of carbon dioxide)':
        emissions_us.append(emissions_dictionary[i][4])




import matplotlib
import matplotlib.pyplot as plt
import numpy as np




x_indexes = np.arange(len(emissions_years))
width = .25
plt.bar(x_indexes, emissions_china, width = width, color ='#444444',label = 'China')
plt.bar(x_indexes + width, emissions_us,  width= width, color ='#008fd5',label = 'U.S')

plt.xticks(ticks= x_indexes, labels= emissions_years)


plt.title('Per Capita Emissions for U.S and China')
plt.xlabel('Year')
plt.ylabel('Emissions per Capita (metric Tons)')
plt.tight_layout()
plt.ylim([0,21])
plt.legend()
plt.show()

import json

with open('/Users/pedroarellano/Documents/GitHub/Environmental-data/China_pop.json', encoding= 'ascii') as f:
    text = f.read()
    china_popdict = json.loads(text)
    china_popdata = china_popdict[1]
china_yearxs =[]
for i in range(len(china_popdata)):
    china_yearxs.append(china_popdata[i]['date'])
china_popvalue=[]
for i in range(len(china_popdata)):
    china_popvalue.append(china_popdata[i]['value'])

with open('/Users/pedroarellano/Documents/GitHub/Environmental-data/US_pop.json', encoding= 'ascii') as f:
    text = f.read()
    us_popdict = json.loads(text)
    us_popdata = us_popdict[1]
us_yearxs =[]
for i in range(len(us_popdata)):
    us_yearxs.append(us_popdata[i]['date'])
us_popdata = us_popdict[1]

us_popvalue =[]
for i in range(len(us_popdata)):
    us_popvalue.append(us_popdata[i]['value'])

us_popvalue.reverse()
china_popvalue.reverse()
us_yearxs.reverse()

x_indexes = np.arange(len(us_yearxs[30:]))
width = .40
plt.bar(x_indexes, china_popvalue[30:], width = width, color ='#444444',label = 'China')
plt.bar(x_indexes + width, us_popvalue[30:],  width= width, color ='#008fd5',label = 'U.S')

plt.xticks(ticks= x_indexes, labels= us_yearxs[30:])

plt.title('Populations of U.S and China')
plt.xlabel('Year')
plt.ylabel('People')
plt.legend()
plt.xticks(rotation = 90,)
plt.show()













with open('/Users/pedroarellano/Documents/GitHub/Environmental-data/1880-2016.json', encoding= 'ascii') as f:
    text = f.read()
    dictionary = json.loads(text)

data = dictionary['data']

years_xs = []
celsius_xs = []
for i in data:
    years_xs.append(int(i))                 #(int(i))
    celsius_xs.append(float(data[i]))                #(isdigit(data[i]))





t = celsius_xs
s = years_xs

fig, ax = plt.subplots()
ax.plot(s, t)


ax.set(xlabel='year', ylabel='Degrees Celsius',
       title='Global Land and Ocean Temperature Anomalies, January-December')

fig.savefig("test.png")
plt.show()

