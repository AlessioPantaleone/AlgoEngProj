import networkx
import networkx as nx
import sys
import time
import csv

# doubling ==[50,100,200,400, 800, 1600, 3200, 6400, 12000,24000]

nn = [1000, 2000]
mm = [0.1, 0.6]

with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['n', 'm', 'hfn', 'hfm', 'time'])

    for n in nn:
        for m in mm:
            G = networkx.erdos_renyi_graph(n, m, seed=42)
            # G = nx.barabasi_albert_graph(X, Y, 33)

            count = []
            best = sys.maxsize

            cpu = time.process_time()

            for attempt in range(10):
                d = nx.coloring.greedy_color(G)
                col = set()
                for j in d.values():
                    col.add(j)
                    count.append(len(col))
                if len(col) < best:
                    best = len(col)
            elapsed = (time.process_time() - cpu)

            writer.writerow([n, m, "High" if n == nn[1] else "Low", "High" if m == mm[1] else "Low", elapsed])
