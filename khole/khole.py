from bluetooth.ble import DiscoveryService
from gattlib import GATTRequester


def main():
    service = DiscoveryService()
    devices = service.discover(2)

    for address, name in devices.items():
        print("name: {}, address: {}".format(name, address))
    req = GATTRequester("20:73:6A:AF:EA:19")
    while True:
        msg = req.read_by_handle(0x2a)[0]
        sensor1 = ord(msg[3]) << 8 | ord(msg[4])
        sensor2 = ord(msg[5]) << 8 | ord(msg[6])
        print("Sensor 1: %d Sensor 2: %d" % (sensor1, sensor2))

if __name__ == "__main__":
    main()
