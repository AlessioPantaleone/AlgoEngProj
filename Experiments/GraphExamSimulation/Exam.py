import random
import statistics
from random import randrange

import sys
import time
from time import sleep

import csv, pandas, numpy, seaborn, configparser

from matplotlib import pyplot

import networkit, networkx


def rng(M, A, B):
    rng.current = (A * rng.current + B) % M
    return rng.current


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

    m = int(configuration["Random"]["m"])
    b = int(configuration["Random"]["b"])
    a = int(configuration["Random"]["a"])
    seed = int(configuration["Random"]["seed"])
    # seed = int(round(time.time() * 1000))

    rng.current = seed

    Nodes = [1000, 2000]
    EdgeProbability = [0.1, 0.3]
    WriteRowToCsv(["n", "e", "HFN", "HFE", "Time"])

    for n in Nodes:
        for p in EdgeProbability:

            Graph = networkx.erdos_renyi_graph(n=n, p=p, seed=seed)
            for (u, v) in Graph.edges():
                Graph.edges[u, v]['weight'] = 1 + round((rng(m, a, b) / m) * 100)
            edges = Graph.number_of_edges()

            ElapsedTimes = []

            for trials in range(int(configuration["DEFAULT"]["trials"])):
                StartTime = time.process_time()
                distances, paths = networkx.single_source_dijkstra(G=Graph,
                                                                   source=random.choice(list(Graph.nodes())),
                                                                   weight="weight")
                Elapsed = time.process_time() - StartTime
                assert max(distances.values()) < n * 100
                ElapsedTimes.append(Elapsed)

            WriteRowToCsv(
                [n, edges, "High" if n == Nodes[1] else "Low", "High" if p == EdgeProbability[1] else "Low",
                 statistics.median(ElapsedTimes)])
