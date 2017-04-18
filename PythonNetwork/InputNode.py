from queue import Queue
# from queue import Queue as SafeQueue

from PythonNetwork.NeuralNode import NeuralNode


# Provides a rolling average
class InputNode(NeuralNode):
    def __init__(self, period_length, data_stream):
        super(InputNode, self).__init__()
        if period_length < 1:
            raise ValueError("Period length must be at least 1")
        self._average = 0
        self._q = Queue(period_length)
        self._buffer = Queue()
        self.subscribe(data_stream)

    def process(self, number):
        if self._q.full():
            self._average -= self._q.get() / self._q.maxsize
        self._q.put_nowait(number)
        self._average += number / self._q.maxsize

    def update_value(self):
        while not self._buffer.empty():
            self.process(self._buffer.get())  # need to block?

    @property
    def value(self):
        if self._q.full():
            return self._average
        return self._average * self._q.maxsize / self._q.qsize()

    @property
    def period_length(self):
        return self._q.maxsize

    def input_changed(self, node):
        # assume node is in self._inputs
        self._buffer.put(node.value)
        super(InputNode, self).input_changed(node)
