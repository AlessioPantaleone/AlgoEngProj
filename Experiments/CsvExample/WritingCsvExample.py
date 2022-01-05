m = 2 ** 32
b = 12345
a = 1103515245

def rng(M=m, A=a, B=b):
    rng.current = (A * rng.current + B) % M
    return rng.current


import csv
import time

#Experiment random
print(f"Seed: {int(round(time.time() * 1000))} ")
rng.current = int(round(time.time() * 1000))
l = 10

header = ["head" + str(i) for i in range(l)]
data1 = [round(rng(m) / m, 2) for i in range(l)]
data2 = [round(rng(m) / m, 2) for i in range(l)]
data3 = [round(rng(m) / m, 2) for i in range(l)]


# # #FOR SIMPLE DATA
data = [header, data1, data2, data3]
filename = 'Write1.csv'
f = open(filename, 'w')

with f:
    writer = csv.writer(f)

    for row in data:
        writer.writerow(row)


# # #FOR COMPLEX OBJECTS
filename2 = 'Write2.csv'
f = open(filename2, 'w')

with f:
    fnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fnames)
    writer.writeheader()
    writer.writerow({'first_name': 'John', 'last_name': 'Smith'})
    writer.writerow({'last_name': 'Brown', 'first_name': 'Robert'})

