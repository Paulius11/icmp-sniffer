from scapy.all import *
from threading import Thread, Event
from time import sleep

from scapy.layers.inet import IP

from mongo import Mongo


class Sniffer(Thread):
    def __init__(self, interface="eth0", filter_protocol="icmp", mongo_protocol=27017):
        super().__init__()

        self.filter_packets = filter_protocol
        self.daemon = True

        self.socket = None
        self.interface = interface
        self.stop_sniffer = Event()
        self.mongo = Mongo(mongo_protocol)

    def run(self):
        self.socket = conf.L2listen(
            type=ETH_P_ALL,
            iface=self.interface,
            filter=self.filter_packets
        )

        sniff(
            opened_socket=self.socket,
            prn=self.print_packet,
            stop_filter=self.should_stop_sniffer
        )

    def join(self, timeout=None):
        self.stop_sniffer.set()
        super().join(timeout)

    def should_stop_sniffer(self, packet):
        return self.stop_sniffer.isSet()

    def print_packet(self, packet):
        ip_layer = packet.getlayer(IP)
        src = ip_layer.src
        dst = ip_layer.dst
        print("[!] New Packet: {src} -> {dst}".format(src=src, dst=dst))
        self.mongo.add_to_db(src, dst)


if __name__ == "__main__":
    sniffer = Sniffer(interface="enp4s0")
    print("[*] Start sniffing...")
    sniffer.start()
    try:
        while True:
            sleep(100)
    except KeyboardInterrupt:
        print("[*] Stop sniffing")
        sniffer.join(2.0)

        if sniffer.is_alive():
            sniffer.socket.close()
