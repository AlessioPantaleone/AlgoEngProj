import time

import networkx.algorithms.tree.mst

from Imports.myimports import *



"""
Mi creo intanto il file di output di tipo csv dove andrò a salvare i risultati dell'esperimento
"""
with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['n', 'm', 'hfn', 'hfm', 'tempo'])  # numero archi totali (m)

    """
    Alcuni dei parametri che dovrei leggere da un file ma che in questo esempio sono hardcoded
    """
    rr = [0.1, 0.3]
    nn = [1000, 3000]

    '''
    Mi preparo una lista di tempi per l'esperimento
    '''
    tempii = []
    for n in nn:
        for r in rr:
            # Creo un Grafo G Con m archi totali
            G = networkx.erdos_renyi_graph(n, r)
            m = G.number_of_edges()

            # Lista per i tempi di questo try
            tempi = []

            for i in range(20):

                cpu = time.process_time()
                d, p = networkx.single_source_dijkstra(G, source=random.choice(list(G.nodes())))
                tempi.append(time.process_time() - cpu)

                # Tutti i percorsi:  d.values()

            elapsed = numpy.median(tempi)  # Faccio la media dei tempi

            tempii.extend(tempi)  # vettore per plot tempi
            print(tempii)

            writer.writerow([n, m, "High" if n == nn[1] else "Low", "High" if r == rr[1] else "Low", elapsed])


# Grafico di tutti i tempi per tutti i try
pyplot.xlabel("n")
pyplot.ylabel("tempi")
pyplot.plot(range(len(tempii)), tempii)
pyplot.plot(200)
pyplot.show()

# Lettura dei dati con pandas
df = pandas.read_csv('output.csv')
print(df)


seaborn.set(style="ticks", color_codes=True)

# Grafico con seaborn
seaborn.lineplot(x="n", y="tempo", style="hfm", data=df, linewidth=5)
pyplot.show()

# Grafico con seaborn
seaborn.lineplot(x="m", y="tempo", style="hfn", data=df, linewidth=5)
pyplot.show()
