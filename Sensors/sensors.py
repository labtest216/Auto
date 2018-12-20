#!/usr/bin/python3
from abc import abstractmethod

from HwModule.hw_modules import HwM


class Sensor(HwM):

    def __init__(self, cfg):
        super().__init__(cfg)
        self.units = cfg["units"]
        self.sample = ""

    def get_sample(self): pass

    def sample_format_display(self): pass

    def set_calibration(self): pass

    def add_interrupts(self): pass

    def get_avg_sample(self): pass



