class TrafficDevice:
    def activate(self):
        print("Device activating...")


class TrafficLight(TrafficDevice):
    def activate(self):
        print("Traffic light cycling: Red -> Green -> Yellow")


class SpeedCamera(TrafficDevice):
    def activate(self):
        print("Speed camera capturing vehicle speed")


class PedestrianSignal(TrafficDevice):
    def activate(self):
        print("Pedestrian signal showing Walk/Don't Walk")


class EmergencySiren(TrafficDevice):
    def activate(self):
        print("Emergency siren sounding alert")


# Test
devices = [
    TrafficLight(),
    SpeedCamera(),
    PedestrianSignal(),
    EmergencySiren()
]

for device in devices:
    device.activate()