#!/usr/bin/python3
from Utils.utils import dprint, f_name


class HwM:
    cfg = {}
    interface = {}

    def __init__(self, cfg):
        self.cfg = cfg
        self.interface = cfg["interface"]
        self.hw_type = cfg["hw_type"]
        self.hw_name = cfg["hw_name"]
        self.interface_name = self.interface["name"]
        self.debug_pre = self.hw_type+" "+self.hw_name+": "+f_name()+": "

    def dprint(self, data):
        dprint(self.debug_pre + data)







