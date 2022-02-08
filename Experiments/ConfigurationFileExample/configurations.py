#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example for reading configs
"""
FILENAME = 'ExperimentConfig.ini'

import configparser

# Per impostare e leggere il file di configurazione dato il filepath
config = configparser.ConfigParser()
config.read('ExperimentConfig.ini')

# Per leggere tutte le sezioni del file di config
print("\nSezioni del file di config:")
print(config.sections())

# Per vedere se una sezione è presente nel file di configurazione
print("\nPresenza di sezioni 'DEFAULT' e 'CIPOLLA' :")
print('DEFAULT' in config)
print('cipolla' in config)

# Per leggere una specifica chiave di una sezione
print("\nLettura della chiave compression da DEFAULT e test da cipolla:")
print(config['DEFAULT']['Compression'])
print(config['cipolla']['test'])

# Per salvare una sezione come un dizionario e leggerlo
print("\nLettura della chiave test da cipolla come dizionario:")
topsecret = config['cipolla']
print(topsecret['test'])

# Per leggere tutte le chiavi di una sezione
print("\nLettura di tutte le chiavi in DEFAULT")
for key in config['DEFAULT']:
    print(key)
