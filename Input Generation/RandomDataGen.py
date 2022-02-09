m = 2 ** 32
b = 12345
a = 1103515245
import time


def rngInt(M=m, A=a, B=b):
    rngInt.current = (A * rngInt.current + B) % M
    return rngInt.current


def rngReal():
    return rngInt()/m


def rngGenerator(datatype="int", vectorsize=1, start=0, stop=1):
    Val = None
    if datatype == "int":
        if vectorsize != 1:
            Val = [start + int(rngReal() * (stop - start + 1)) for i in range(vectorsize)]
        else:
            Val = start + int(rngReal() * (stop - start + 1))
    if datatype == "double":
        if vectorsize != 1:
            Val = [start + (rngReal() * (stop - start)) for i in range(vectorsize)]
        else:
            Val = start + (rngReal() * (stop - start))
    return Val



# setting the seed:
# rng.current = 1641383494547 (a good number)
rngInt.current = int(round(time.time() * 1000))

#Random integer
Value = rngInt()

#Random double between 0 and 1
Value = rngReal()

#Random integer between start and stop
start = 10
stop = 30
Value = start + int(rngReal() * (stop - start + 1))

#Random double between start and stop
start = 10
stop = 30
Value = start + (rngReal() * (stop - start))

# vector of random integers
Value = [rngInt() for i in range(10)]

# vector of random floats
Value = [rngInt() / m for i in range(10)]

# vector of random integers within range start,end
start = 5
end = 25
Value = [start + round((rngInt() / m) * (end - start + 1)) for i in range(10)]

# vector of random floats within range start,end
start = 5
end = 25
Value = [start + (rngInt() / m) * (end - start) for i in range(10)]

print("///////////////")
print("Randint")
print(rngGenerator(datatype="int",start=10,stop=70))
print("Randfloat")
print(rngGenerator(datatype="double",start=10,stop=70))
print("Randintvector")
print(rngGenerator(datatype="int",vectorsize=7,start=10,stop=70))
print("Randintfloat")
print(rngGenerator(datatype="double",vectorsize=7,start=10,stop=70))


