class InputStream(object):
    def __init__(self, path_to_file):
        self._value = None
        self._outputs = []
        self._path = path_to_file
        self._buffer = []
        self._counter = 0

    def initialize(self):
        file = open(self._path, "r")
        for line in file:
            self._buffer.append(float(line))
        file.close()

    @property
    def value(self):
        return self._value

    @property
    def dirty(self):
        return False

    def counter_subscribe(self, node):
        self._outputs.append(node)

    def read_and_broadcast(self):
        self._value = self._buffer[self._counter]
        self._counter += 1
        for o in self._outputs:
            o.input_changed(self)
        return self._counter < len(self._buffer)
