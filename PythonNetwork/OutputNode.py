from PythonNetwork.NeuralNode import NeuralNode


class OutputNode(NeuralNode):
    def __init__(self, min_threshold, max_threshold):
        super(OutputNode, self).__init__()
        self._min = min_threshold
        self._max = max_threshold
        self._sum = None

    @property
    def value(self):
        return min(max(self._sum, self._min), self._max)

    def update_value(self):
        self._sum = sum([i.value for i in self._inputs])
