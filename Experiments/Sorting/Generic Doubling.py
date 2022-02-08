from Imports.myimports import *


if __name__ == "__main__":

    n = []
    timers = []
    ratios = []

    for iterations in range(18):
        IterationTimers = []
        IterationRatios = []

        for attempts in range(3):
            A = []
            B = []
            currentlength = pow(2, iterations + 1)

            while len(A) < currentlength:
                A.append(randrange(pow(2, iterations + 1)))
            if attempts == 1:
                n.append(currentlength)
            # Ask standard python to sort the array A
            B = (sorted(A)).copy()

            Start = timer()
            quickSort(A, pivotposition="random")  # Here you can insert any algorithm
            ExpTime = timer() - Start

            IterationTimers.append(ExpTime)
            IterationRatios.append(ExpTime/currentlength)

            print(A)

            assert A == B # Check if the algo is correct
            print(f"Iteration {iterations} :", end="")
            print(f"Experiment Time :[{ExpTime:.5f}],Time/Length Ratio :{ExpTime/currentlength:.10f}", end="")
            print("")
        timers.append(sum(IterationTimers) / len(IterationTimers))
        ratios.append(sum(IterationRatios) / len(IterationRatios))

    print(n)
    print(timers)
    print(ratios)

    pyplot.plot(n, timers)
    pyplot.plot(n, ratios)
    pyplot.show()
