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
for i in data['state']:
    active.append(i['active'])
    death.append(i['death'])
    total.append(i['total'])

labels = ['A&N Islnads','Andhra P','Arunanchal P','Assam','Bihar','Chandigarh','Chhattisgarh','Daman & Diu','Delhi','Goa','Gujarat','Haryana','HP','J&K','Jharkhand','Karnataka','Kerala','Ladakh','MP','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telegana','Tripura','Uttarakhand','UP','West Bengal']
x =np.arange(0,875,25)
f,ax=plt.subplots(figsize=(50,15))
width = 2.0
plt.xticks(x,labels[:35])
plt.bar(x-4,total[:35],width,color='red',label='Total Cases')
plt.bar(x,active[:35],width,color='green',label='Active Cases')
plt.bar(x+4,death[:35],width,color='black',label='Deceased')
plt.title('Covid-19 Statistics')
plt.ylabel('Cases')
plt.xlabel('States')
plt.legend()
plt.autoscale(True)
plt.show()
