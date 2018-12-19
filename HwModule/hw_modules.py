#!/usr/bin/python3


class HwM:
    cfg = {}
    interface = {}

    def __init__(self, cfg):
        self.cfg = cfg
        self.interface = cfg["interface"]
        self.hw_type = cfg["hw_type"]
        self.interface_name = self.interface["name"]







