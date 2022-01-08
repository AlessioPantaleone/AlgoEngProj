import random


if __name__ == "__main__":
    # T ia any vector
    T = [17,8,3,4,5,1,7,9]
    print(T)
    # some predefined shuffling from python
    random.shuffle(T)
    print(T)

    # some predefined from python for generation given an integer n
    n = 8
    print("\nRANDOM INTEGER:", random.randrange(n))
    print(f"RANDOM FLOAT <=n (n = {n}):", random.random() * n)
    print("RANDOM FROM T:", random.choice(T))
