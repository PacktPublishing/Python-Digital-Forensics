#!/usr/bin/python3

import subprocess
import sys


class Ping:
    def __init__(self):
        self.address = '192.168.56.'

    def main(self):
        for x in range(100, 102):
            p = subprocess.Popen(
                "ping -c 1 {0}{1}".format(
                    self.address, x), shell=True, stderr=subprocess.PIPE)

            while True:
                out = p.stderr.read(1)
                if not out and p.poll() is not None:
                    break
                if out:
                    sys.stdout.write(out)
                    sys.stdout.flush()


if __name__ == '__main__':
    ping = Ping()
    ping.main()
