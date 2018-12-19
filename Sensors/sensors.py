#!/usr/bin/python3
from abc import abstractmethod

from HwModule.hw_modules import HwModule


class Sensor(HwModule):

    """Base class for sensor"""

    def get_sample(self): pass

    def set_calibration(self): pass
