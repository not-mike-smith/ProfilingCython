import math


def generate_data(folder):
    file = open(folder + "\\data1.qqq", "w")  # sigmoid with periodic aberrations
    len1 = 1000000  # 1e6
    for i in range(len1):
        i -= len1/2
        i = 1.0/(1.0 + math.exp(-i/(len1/5.0)))
        i += 0.1 * math.sin(i/1700.0)
        i += 0.025 * math.cos(i / 5300.0)
        file.write(str(i) + "\n")
    file.close()
    len2 = 100000  # 1e5
    file = open(folder + "\\data2.qqq", "w")  # straight line from 1 to -1
    for i in range(len2):
        f = float(i)
        f = 1 + -2 * f / len2
        file.write(str(f) + "\n")
    file.close()
    len3 = 100000  # 1e5
    file = open(folder + "\\data3.qqq", "w")  # Arnold tongue with K=math.pi
    theta = 0
    omega = 0.1
    for _ in range(len3):
        theta = theta + omega - 0.5*math.sin(2 * math.pi * theta)
        file.write(str(theta) + "\n")
    file.close()
    len4 = 1000000  # 1 e6
    size = 2147483648  # 2^31
    c = 7919.0 / 7907.0
    b = 31.0 / 23.0
    z = 0
    file = open(folder + "\\data4.qqq", "w")  # Steady increase to 10 with chaotic noise
    for i in range(len4):
        z = (z*z + b*z + c) % size
        i = (float(i) / len4 * 10) + (float(z) / size)
        file.write(str(i) + "\n")
    file.close()
