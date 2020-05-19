from time import sleep

from sniffer import Sniffer


def run_sniffer(**args):
    sniffer = Sniffer(**args)
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


run_sniffer(interface="enp4s0", filter_protocol="icmp", mongo_protocol=27017)
