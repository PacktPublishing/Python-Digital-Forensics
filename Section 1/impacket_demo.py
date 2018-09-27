#!/usr/bin/python2.7

import sys
from pcapy import open_offline, open_live
from impacket.ImpactDecoder import EthDecoder


class ImpacketDemo(object):
    def __init__(self):
        super(ImpacketDemo, self).__init__()
        pass

    def read_packet(self, hdr, data):
        decoder = EthDecoder()
        ether = decoder.decode(data)
        ip = ether.child()
        tcp = ip.child()

        try:
            print ip.get_ip_src()
            print tcp.get_th_sport()
            print ip.get_ip_dst()
            print tcp.get_th_dport()

        except:
            print "error"

    def main(self, pcap_file):
        pcap = open_offline(pcap_file)
        pcap.loop(0, self.read_packet)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        sys.exit("Usage: %s <filename>" % sys.argv[0])

    demo = ImpacketDemo()
    demo.main(sys.argv[1])
