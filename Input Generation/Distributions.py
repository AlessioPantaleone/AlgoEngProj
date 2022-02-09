import time

from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

if __name__ == "__main__":

    print("DISTRIBUTIONS:\n"
          "NORMAL : RED\n"
          "BINOMIAL : BLACK\n"
          "POISSON : GREEN\n"
          "UNIFORM : BLUE\n")

    time.sleep(0.1)

    sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal', color="RED")
    sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial', color="BLACK")
    sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson', color="GREEN")
    sns.distplot(random.uniform(low=20, high=80, size=1000), hist=False, label='uniform', color="BLUE")
    plt.show()



