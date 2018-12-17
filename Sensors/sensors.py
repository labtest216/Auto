#!/usr/bin/python3
from abc import abstractmethod

from HwModule.hw_modules import HwModule


class Sensor(HwModule):
    """Base class for sensor"""


    @abstractmethod
    def get_sample(self): pass

    @abstractmethod
    def set_calibration(self): pass
