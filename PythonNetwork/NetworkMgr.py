from collections import OrderedDict


_node_queue = OrderedDict()
_all_nodes = []


def register_node(node):
    _all_nodes.append(node)


def enqueue(node):
    _node_queue[node] = None


def run_one_node():
    q = _node_queue.keys()
    node = next(n for n in q if n.inputs_not_dirty)
    # if the next() call raises StopIteration, then we should exit b/c that means no node is ready to execute.
    del _node_queue[node]
    node.execute()
    return len(_node_queue) > 0
