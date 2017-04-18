def create_generator():
    """
    :return: pseudo-random number between -1 and 1
    """
    c = 3083.0 / 4339.0
    b = 947.0 / 2663.0
    z = 0
    size = 2147483648  # 2^31
    while True:
        z = (z * z + b * z + c) % size
        yield (float(z) / (size / 2)) - 1
