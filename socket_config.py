from pyorient import OrientSocket
class Socket(OrientSocket):
    def __init__(self, host, port, protocol=36, timeout=300):
        super().__init__(host, port)
        self.protocol = protocol
        self.host = host
        self.port = port
        self.timeout = timeout
    def connect(self):
        self._socket.connect((self.host, self.port))
        _value = self._socket.recv(2)
        self.connected = True