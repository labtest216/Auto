#!/usr/bin/python3
from abc import abstractmethod

from HwModule.hw_modules import HwModule


class Camera(HwModule):
    """Base class for camera."""

    @abstractmethod
    def take_snapshot(self): pass

    @abstractmethod
    def set_calibration(self): pass