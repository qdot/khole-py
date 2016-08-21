from bluetooth.ble import DiscoveryService
from gattlib import GATTRequester


class kHole(object):
    def __init__(self):
        self.device = None

    def connect_via_scan(self):
        service = DiscoveryService()
        devices = service.discover(2)
        for address, name in devices.items():
            if name == "kGoal":
                self.device = GATTRequester(address)
                return True
        return False

    def get_reading(self):
        msg = self.device.read_by_handle(0x2a)[0]
        sensor1 = ord(msg[3]) << 8 | ord(msg[4])
        sensor2 = ord(msg[5]) << 8 | ord(msg[6])
        return (sensor1, sensor2)

    def set_squeeze_pillow(self, on):
        if on:
            self.device.write_by_handle(0x41, str(bytearray([0x00, 0x01, 0x07, 0x00, 0x1b, 0x00, 0x00, 0x96, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])))
        else:
            self.device.write_by_handle(0x41, str(bytearray([0x00, 0x01, 0x07, 0x00, 0x00, 0x00, 0x00, 0x96, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])))

    def set_control_arm(self, on):
        if on:
            self.device.write_by_handle(0x41, str(bytearray([0x00, 0x02, 0x07, 0x00, 0x1b, 0x00, 0x00, 0x96, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])))
        else:
            self.device.write_by_handle(0x41, str(bytearray([0x00, 0x02, 0x07, 0x00, 0x00, 0x00, 0x00, 0x96, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])))


def main():
    k = kHole()
    if not k.connect_via_scan():
        print("Can't find kgoal device!")
        return
    print("Turning off both motors")
    k.set_control_arm(False)
    k.set_squeeze_pillow(False)

    def wait_for_reading():
        while True:
            sensors = k.get_reading()
            if sensors[0] > 500:
                break

    print("Press in to turn on control arm motor")
    wait_for_reading()
    k.set_control_arm(True)
    print("Press in to turn on squeeze pillow motor")
    wait_for_reading()
    k.set_control_arm(False)
    k.set_squeeze_pillow(True)
    print("Press in to turn on both motors")
    wait_for_reading()
    k.set_control_arm(True)
    k.set_squeeze_pillow(True)

if __name__ == "__main__":
    main()
