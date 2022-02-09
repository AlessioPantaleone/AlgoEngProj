import random
import statistics
from random import randrange

import os
import sys
import time
from time import sleep

import csv, pandas, numpy, seaborn, configparser

from matplotlib import pyplot

import networkit, networkx

def WriteRowToCsv(row, filename="output.csv"):
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)


def ParseConfig(filename="ExperimentConfig.ini"):
    config = configparser.ConfigParser()
    config.read(filename)
    return config


if __name__ == "__main__":
    configuration = ParseConfig()
    os.remove("output.csv")
