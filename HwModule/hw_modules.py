#!/usr/bin/python3
import logging
from Utils.utils import *


class HwModule(object):
    """Abstract base class for HW module."""
    logger_handler = logging.getLogger(__name__)
    file_handler = logging.FileHandler("hw_modules.log")
    formatter = logging.Formatter.formatTime
    file = os.path.basename(__file__)
    cfg = {}
    com = object

    def __init__(self, cfg):
        self.cfg = cfg
        self.interface = self.cfg["interface"]
        self.init_com()


    def get_name(self):
        return self.name


    def get_hw_type(self):
        return self.hw_type

    def init_com(self): pass

# HW communication type.


    def init_com_i2c(self):
        print("not imp")





