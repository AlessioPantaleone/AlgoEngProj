m = 2 ** 32
b = 12345
a = 1103515245


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


"""
def rngInt(M, A, B):
    rngInt.current = (A * rngInt.current + B) % M
    return rngInt.current


def rngGenerator(M, A, B, datatype="int", vectorsize=1, start=0, stop=1):
    Val = None
    if datatype == "int":
        if vectorsize != 1:
            Val = [start + int((rngInt(M, A, B) / m) * (stop - start + 1)) for i in range(vectorsize)]
        else:
            Val = start + int((rngInt(M, A, B) / m) * (stop - start + 1))
    if datatype == "double":
        if vectorsize != 1:
            Val = [start + ((rngInt(M, A, B) / m) * (stop - start)) for i in range(vectorsize)]
        else:
            Val = start + ((rngInt(M, A, B) / m) * (stop - start))
    return Val
    
    
#   Preparing just in case i need some random input
m = int(configuration["Random"]["m"])
b = int(configuration["Random"]["b"])
a = int(configuration["Random"]["a"])
seed = int(configuration["Random"]["seed"])
# seed = int(round(time.time() * 1000))
rngInt.current = seed
"""