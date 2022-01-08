from collections import Counter
import random

EVENTS = ["WIN", "LOSE", "TIE"]

P = [0.1, 0.1, 0.8]
prob = []

for k in range(len(P)):
    prob.append(sum([P[i] for i in range(k + 1)]))


OUTCOME = []

for i in range(100):
    r = random.random()
    for p in prob:
        if r < p:
            OUTCOME.append(EVENTS[prob.index(p)])
            break
print(OUTCOME)
print(Counter(OUTCOME))
