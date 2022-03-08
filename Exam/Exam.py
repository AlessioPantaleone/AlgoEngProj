import configparser
import csv
import numpy
import os
import random
import time
import networkx


def WriteRowToCsv(row, filename="output.csv"):
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)


def ParseConfig(filename="ExperimentConfig.ini"):
    config = configparser.ConfigParser()
    config.read(filename)
    return config


def BFS(G, S, w):
    Q = [S]
    M = [0 for _ in range(G.number_of_nodes())]
    M[S] = 1
    while Q:
        Exctracted = Q.pop()
        time.sleep(w)
        for neighbor in G.neighbors(Exctracted):
            if M[neighbor] != 1:
                M[neighbor] = 1
                Q.insert(0, neighbor)
    return M


if __name__ == "__main__":
    configuration = ParseConfig()
    if os.path.exists("output.csv"):
        os.remove("output.csv")

    seed = int(configuration["Random"]["seed"])
    # seed = int(round(time.time() * 1000))

    StartingNodes = int(configuration["DEFAULT"]["StartingNodes"])
    StartingEdges = int(configuration["DEFAULT"]["StartingEdges"])

    WaitingTime = 0.001
    WriteRowToCsv(["Nodes", "Edges", "Time", "MarkedNodes", "Seed"])

    n = [StartingNodes, 2 * StartingNodes, 4 * StartingNodes, 8 * StartingNodes, 16 * StartingNodes]
    m = [StartingEdges, 2 * StartingEdges, 4 * StartingEdges, 8 * StartingEdges, 16 * StartingEdges]

    for NodeNumber in n:
        for EdgeNumber in m:
            if EdgeNumber >= NodeNumber:
                Graph = networkx.gnm_random_graph(NodeNumber, EdgeNumber, seed=seed)
                assert Graph.number_of_edges() == EdgeNumber
                Times = []
                MarkedNodes = []
                for t in range(int(configuration["DEFAULT"]["Trials"])):
                    print(f"Trial {t + 1} with {NodeNumber} nodes and {EdgeNumber} Edges")
                    Source = random.choice(list(Graph.nodes()))
                    StartTime = time.process_time()
                    P = BFS(Graph, Source, WaitingTime)
                    Times.append(time.process_time() - StartTime)
                    MarkedNodes.append(P.count(1))
                WriteRowToCsv([NodeNumber, EdgeNumber, numpy.median(Times), MarkedNodes, seed])
