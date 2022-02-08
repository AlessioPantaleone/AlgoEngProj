import random
from random import randrange

import sys
import time
from time import sleep

import csv, pandas, numpy, seaborn, configparser

from matplotlib import pyplot

import networkit, networkx

def rng(M=2 ** 32, A=1103515245, B=12345):
    rng.current = (A * rng.current + B) % M
    return rng.current


def WriteDataToCsv(data, filename="output.csv"):
    with open(filename, 'w+') as csvfile:
        writer = csv.writer(csvfile)
        for row in data:
            writer.writerow(row)


def WriteRowToCsv(row, filename="output.csv"):
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)


def ParseConfig(filename="ExperimentConfig.ini"):
    config = configparser.ConfigParser()
    config.read(filename)
    return config

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

if __name__ == "__main__":
    rng.current = int(round(time.time() * 1000))
    configuration = ParseConfig()

    # Doubling Experiment su mergesort

    n = [2, 4, 6, 8, 16, 32, 64, 128, 256,3000]

    WriteRowToCsv(["n", "time", "ratio"])

    for factor in n:
        Array = [rng() for i in range(factor)]
        SortedArray = Array.copy()
        SortedArray.sort()

        StartTime = time.process_time()
        insertionSort(Array)
        Elapsed = time.process_time() - StartTime

        assert Array == SortedArray

        WriteRowToCsv([factor, Elapsed, Elapsed/factor])























