#!/usr/bin/python3
from HwModule.hw_modules import HwModule
#from abc import ABC, ABCMeta, abstractmethod


class RelayBoard(HwModule):
    """Base class for switches card."""

    #@abstractmethod
    def set_switch(self, switch_num, mode): pass

    def set_water_on(self):
        self.set_switch(self.cfg["Connections"]["waterpump_switch"]["sw"], 1)

    def set_water_off(self):
        self.set_switch(self.cfg["waterpump_switch"], 0)



