#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:08:12 2021

@author: luca
"""

import csv
import random
import pandas as pd
from configparser import ConfigParser
import os.path

config = ConfigParser()



if os.path.isfile('./es0_dati.csv'):
    config.read('es0_dati.ini')
    print('File caricato correttamente')

else:
    config['DEFAULT'] = {'lunghezzavettore': '5','numerorighe': '8'}
    
    with open('es0_dati.ini', 'w') as configfile:
        config.write(configfile)
    
    config.read('es0_dati.ini')
    print('File generato correttamente')


m = int(config['DEFAULT']['numerorighe'])
print(type(m))

header = ["Dato"+str(i) for i in range(m)]

data1 = [int(random.randrange(10)) for i in range(m)]
data2 = [int(random.randrange(10)) for i in range(m)]
data3 = [int(random.randrange(10)) for i in range(m)]
filename = 'es0_dati.csv'

data=[header, data1, data2, data3]

print(data)

with open(filename, 'w') as f:
 
    writer = csv.writer(f)
    
    for row in data:
        writer.writerow(row)


df = pd.read_csv('es0_dati.csv')

print(df) 
