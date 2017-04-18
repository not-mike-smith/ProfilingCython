from InputStream import InputStream
from OutputStream import OutputStream
from PythonNetwork.CalculationNode import CalculationNode
from PythonNetwork.InputNode import InputNode
import ProceduralPseudoRandom as ppr
import itertools
from PythonNetwork.OutputNode import OutputNode


pseudo_random = ppr.create_generator()


def create_calculation_node(node1, node2, node3):
    ret = CalculationNode(next(pseudo_random), next(pseudo_random), next(pseudo_random), 1024)
    ret.subscribe(node1)
    ret.subscribe(node2)
    ret.subscribe(node3)
    return ret


def create_calculation_nodes1(node_list):
    ret = []
    for comb in itertools.combinations(node_list, 3):
        ret.append(create_calculation_node(comb[0], comb[1], comb[2]))
    return ret


def create_calculation_nodes2(node_list):
    ret = []
    i = 0
    while i <= len(node_list) - 3:
        ret.append(create_calculation_node(node_list[i], node_list[i+1], node_list[i+2]))
        i += 3
    return ret


def generate(folder):
    data_stream1 = InputStream(folder + "\\data1.qqq")
    data_stream2 = InputStream(folder + "\\data2.qqq")
    data_stream3 = InputStream(folder + "\\data3.qqq")
    data_stream4 = InputStream(folder + "\\data4.qqq")
    data_stream1.initialize()
    data_stream2.initialize()
    data_stream3.initialize()
    data_stream4.initialize()
    node01 = InputNode(100, data_stream1)
    node02 = InputNode(10, data_stream2)
    node03 = InputNode(10, data_stream3)
    node04 = InputNode(2, data_stream4)
    node05 = InputNode(100, data_stream4)
    gen1_calc_nodes = create_calculation_nodes1([node01, node02, node03, node04, node05])
    gen2_calc_nodes = create_calculation_nodes1(gen1_calc_nodes)
    gen3_calc_nodes = create_calculation_nodes2(gen2_calc_nodes)
    limit = 1073741824  # 2^30
    node06 = OutputNode(0, limit)
    node07 = OutputNode(-limit, limit)
    l = len(gen3_calc_nodes)
    for i in range(0, int(2.0/3.0 * l)):
        node06.subscribe(gen3_calc_nodes[i])
    for i in range(int(1.0/3.0 * l), l):
        node07.subscribe(gen3_calc_nodes[i])
    output1 = OutputStream(folder + "\\output1.qqq")
    output2 = OutputStream(folder + "\\output2.qqq")
    node06.counter_subscribe(output1)
    node07.counter_subscribe(output2)
    return data_stream1, data_stream2, data_stream3, data_stream4, output1, output2
