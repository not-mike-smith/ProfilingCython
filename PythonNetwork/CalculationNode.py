from PythonNetwork.NeuralNode import NeuralNode


class CalculationNode(NeuralNode):
    def __init__(self, a, b, c, limit):
        super(CalculationNode, self).__init__()
        self._a = a
        self._b = b
        self._c = c
        self._range = limit
        self._value = None

    @property
    def value(self):
        return self._value

    def update_value(self):
        if len(self._inputs) != 3:
            raise RuntimeError("CalculationNode should have 3 inputs, but has {}".format(len(self._inputs)))
        self._value = (self._a * self._inputs[0].value +
                       self._b * self._inputs[1].value +
                       self._c * self._inputs[2].value) % self._range
