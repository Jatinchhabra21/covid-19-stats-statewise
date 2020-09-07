
import matplotlib
from urllib import request 
import json
import matplotlib.pyplot as plt
import numpy as np
cases ={}
active = []
death = []
total = []
base_url = "http://covid19-india-adhikansh.herokuapp.com/states"
raw_data = request.urlopen(base_url)
data = json.load(raw_data)
# print('State    Total    Active    Cured    Deaths')
for i in data['state']:
#     print(i['name'],i['total'],i['active'],i['cured'],i['death'])
    cases[i['name']] = i['active']
    active.append(i['active'])
    death.append(i['death'])
    total.append(i['total'])
labels = list(cases.keys())
x =np.arange(0,770,22)
f,ax=plt.subplots(figsize=(50,15))
width = 2.0
plt.xticks(x,labels[1:])
plt.bar(x-18,total[1:],width,color='red',label='Total Cases')
plt.bar(x-16,active[1:],width,color='green',label='Active Cases',align='edge')
plt.bar(x-14,death[1:],width,color='black',label='Deceased',align='edge')
plt.title('Covid-19 Statistics')
plt.ylabel('Cases')
plt.xlabel('States')
plt.legend()
plt.autoscale(True)
plt.show()






