#!/usr/bin/python3

import Adafruit_BBIO.GPIO as GPIO
from Sensors.sensors import Sensor



class WaterLevel(Sensor):
    """
    Sensor measure water level.
    FullY  ---- : Pins=111.
    Half+ ---: Pins=011.
    Half- --:Pins=001.
    Empty -:Pins=000.
    Interrupt too fully Pins=111.
    Interrupt too empty Pins=000.
    """
    def __init__(self, cfg):
        super().__init__(cfg)

        pins = str(self.cfg["interface"]["com"]).strip(',')
        self.full = pins[0]
        self.half = pins[1]
        self.empt = pins[2]

        self.set_calibration()
        self.add_interrupts()

    def set_calibration(self):
        GPIO.setup(self.full, GPIO.IN)
        GPIO.setup(self.half, GPIO.IN)
        GPIO.setup(self.empt, GPIO.IN)

    def sample_format_display(self):
        return str(self.sample)+" "+self.cfg["units"]

    def get_sample(self):
        if GPIO.input(self.full) and GPIO.input(self.half) and GPIO.input(self.empt):
            self.sample = "FULLY"
        elif not GPIO.input(self.full) and GPIO.input(self.half) and GPIO.input(self.empt):
            self.sample = "HALF+"
        elif not GPIO.input(self.full) and not GPIO.input(self.half) and GPIO.input(self.empt):
            self.sample = "HALF-"
        elif not GPIO.input(self.full) and not GPIO.input(self.half) and not GPIO.input(self.empt):
            self.sample = "EMPTY"
        else:
            self.sample = "UNKNOWN MODE"
        self.dprint(self.sample_format_display())
        return self.sample

    def add_interrupts(self):
        GPIO.add_event_detect(self.empt, GPIO.FALLING, callback=self.water_is_empty(), bouncetime=300)
        GPIO.add_event_detect(self.full, GPIO.RISING, callback=self.water_is_full(), bouncetime=300)

    def water_is_full(self):
        self.dprint(self.get_sample())
        return True

    def water_is_empty(self):
        self.dprint(self.get_sample())
        return True