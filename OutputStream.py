class OutputStream(object):
    def __init__(self, path_to_file):
        self._path = path_to_file
        self._buffer = []

    def input_changed(self, node):
        self._buffer.append(node.value)

    def publish(self):
        file = open(self._path, "w")
        file.writelines([str(value) + '\n' for value in self._buffer])
        file.close()
