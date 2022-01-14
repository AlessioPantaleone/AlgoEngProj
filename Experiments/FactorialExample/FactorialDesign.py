from Imports.myimports import *



def fakealgorithm(m, n, r):
    sleep(int(((m + 3) * 4 * r) / (1 + n)) / 500)


if __name__ == "__main__":

    m = [10, 20]
    n = [5, 10]
    r = [20, 40]

    with open('experiment', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["F1", "F2", "F3", "hF1", "hF2", "hF3", "Time"])

        for mm in m:
            for nn in n:
                for rr in r:  # all combinations

                    cpu = timer()
                    fakealgorithm(mm, nn, rr)
                    elapsed = timer() - cpu

                    writer.writerow([mm, nn, rr, "High" if mm == m[1] else "Low", "High" if nn == n[1] else "Low",
                                     "High" if rr == r[1] else "Low", elapsed])

    df = pandas.read_csv('experiment')
    print(df)
