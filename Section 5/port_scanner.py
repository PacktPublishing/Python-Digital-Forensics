#!/usr/bin/python3

import socket
import sys
import argparse


class PortScan:
    def __init__(self):
        self.__author__ = "kd8bny@gmail.com"

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(
            description="Scan top ports of a device")
        parser.add_argument("address", help="IP address")
        parser.add_argument(
            "-p", "--ports", nargs='*', help="Ports to scan " +
            "Supports values 1,2 or range 1-5")

        return parser.parse_args()

    def _scan(self, ip, ports):
        try:
            for port in ports:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    print("Port {}: Open".format(port))

        except KeyboardInterrupt:
            sys.exit("Scan terminated")

        except socket.error:
            sys.exit("Couldn't connect to server")

        finally:
            sock.close()

    def main(self):
        args = self.get_args()

        ports = list()
        if not args.ports:
            ports = range(1, 1025)
        else:
            for entry in args.ports:
                if '-' in entry:
                    values = [int(x) for x in entry.split('-')]
                    [ports.append(x) for x in range(values[0], values[1] + 1)]
                else:
                    ports.append(int(entry))

        self._scan(args.address, ports)


if __name__ == '__main__':
    port_scan = PortScan()
    port_scan.main()
