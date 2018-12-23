#!/usr/bin/python3


from Sensors.sensors import Sensor


class Sens(Sensor):
    """
        Sensor measure .

        """

    def __init__(self, cfg):
        super().__init__(cfg)
        self.set_calibration()
        self.name = "sens"

    def get_sample(self):
        self.name = "s"
        return "sens"
