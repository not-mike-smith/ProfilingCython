from abc import abstractmethod
from PythonNetwork import NetworkMgr


class NeuralNode(object):
    def __init__(self):
        self._inputs = []
        self._outputs = []
        self._dirty = False
        NetworkMgr.register_node(self)

    def subscribe(self, node):
        self._inputs.append(node)
        node.counter_subscribe(self)

    def counter_subscribe(self, node):
        self._outputs.append(node)

    @property
    def dirty(self):
        return self._dirty

    @property
    def inputs(self):
        return self._inputs.copy()

    @property
    def outputs(self):
        return self._outputs.copy()

    @property
    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def update_value(self):
        pass

    def execute(self):
        self.update_value()
        self._dirty = False
        for subscriber in self._outputs:
            subscriber.input_changed(self)

    def input_changed(self, node):
        self._dirty = True
        NetworkMgr.enqueue(self)

    @property
    def inputs_not_dirty(self):
        for i in self._inputs:
            if i.dirty:
                return False
        return True
