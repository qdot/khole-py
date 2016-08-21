from khole import kHoleDevice


def main():
    k = kHoleDevice()
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
    print("Both motors now off")
    print("Press in to turn on control arm motor")
    wait_for_reading()
    k.set_control_arm(True)
    print("Control arm motor now on")
    print("Press in to turn on squeeze pillow motor")
    wait_for_reading()
    k.set_control_arm(False)
    k.set_squeeze_pillow(True)
    print("Squeeze pillow motor now on")
    print("Press in to turn on both motors")
    wait_for_reading()
    k.set_control_arm(True)
    k.set_squeeze_pillow(True)
    print("Both motors now on")

if __name__ == "__main__":
    main()
