"""
Doubling Experiment for insertionsort
"""

from random import randrange
import matplotlib.pyplot as plt


def insertionSort(arr):
    counter = 0
    for i in range(1, len(arr)):
        counter += 1
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            counter += 1
            j -= 1
        arr[j + 1] = key
    print("n:", len(arr), "COUNTER:", counter, "COUNTER/n:", round(counter / len(arr), 3))
    return counter, round(counter / len(arr), 3)


if __name__ == "__main__":

    n = []
    timers = []
    ratios = []
    for iterations in range(15):
        for attempts in range(3):
            A = []
            B = []
            newlenght = pow(2, iterations + 1)

            while len(A) < newlenght:
                A.append(randrange(pow(2, iterations + 1)))
            n.append(len(A))

            # Ask standard python to sort the array A
            B = (sorted(A)).copy()
            # x, y are the "Timer" and the "Timer/ArrLength"
            x, y = insertionSort(A)
            assert A == B

            timers.append(x)
            ratios.append(y)

    plt.plot(n, timers)
    plt.plot(n, ratios)
    plt.show()
