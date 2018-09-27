#!/usr/bin/python3


import sys
from scapy.all import *


class scapy_demo(object):
    """docstring for scapy_demo"""

    def __init__(self):
        super(scapy_demo, self).__init__()
        pass

    def main(self, pcap_file):
        pcap = rdpcap(pcap_file)
        print(pcap.sessions())


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit("Feed me pcap!!!  python3 scapy_demo <pcap>")

    scapy_demo = scapy_demo()
    scapy_demo.main(sys.argv[1])
