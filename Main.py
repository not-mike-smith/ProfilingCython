import NetworkGenerator
from DataGenerator import DataGenerator
import matplotlib.pyplot as plt
from InputStream import InputStream
from PythonNetwork.InputNode import InputNode
import PythonNetwork.NetworkMgr as NetworkMgr


folder = "C:\\users\\michael\\documents\\neural_network_data"


# DataGenerator.generate_data(folder)
ds1, ds2, ds3, ds4, os1, os2 = NetworkGenerator.generate(folder)
more_data = True
while more_data:
    for _ in range(10):
        more_data = ds1.read_and_broadcast() and more_data
        more_data = ds4.read_and_broadcast() and more_data
    more_data = ds2.read_and_broadcast() and more_data
    more_data = ds3.read_and_broadcast() and more_data
    more_nodes = True
    while more_nodes:
        more_nodes = NetworkMgr.run_one_node()
os1.publish()
os2.publish()
