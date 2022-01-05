m = 2 ** 32
b = 12345
a = 1103515245

def rng(M=m, A=a, B=b):
    rng.current = (A * rng.current + B) % M
    return rng.current


import time

# setting the seed:
# rng.current = 1641383494547 (a good number)
rng.current = int(round(time.time() * 1000))

# vector of random integers
vector = [rng(m) for i in range(10)]
print(vector)

# vector of random floats
vector = [rng(m) / m for i in range(10)]
print(vector)

# vector of random integers within range start,end
start = 5
end = 25
vector = [start + round((rng(m) / m) * (end - start + 1)) for i in range(10)]
print(vector)

# vector of random floats within range start,end
start = 5
end = 25
vector = [start + (rng(m) / m) * (end - start) for i in range(10)]
print(vector)
