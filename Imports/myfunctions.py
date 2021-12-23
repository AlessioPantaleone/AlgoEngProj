from myimports import *


def csvWrite(n, t, file="result.csv"):
    f = open(file, 'w+')
    writer = csv.writer(f)
    writer.writerow(["I", "T"])

    f.close()
    ps = pandas.read_csv(file)
    print(ps)
    print("")
    print("--------------------")
    print("")


def configParser(file="input.ini"):
    config = configparser.ConfigParser()
    config.read(file)
    return
