from time import sleep

try:
    from sniffer import Sniffer
except ImportError:
    from .sniffer import Sniffer


def main(**args):
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


if __name__ == "__main__":
    main()
