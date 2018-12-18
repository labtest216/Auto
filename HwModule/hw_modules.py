import logging
import os


class HwModule:
    """Abstract base class for HW module."""
    #logger_handler = logging.getLogger(__name__)
    #file_handler = logging.FileHandler("hw_modules.log")
    #formatter = logging.Formatter.formatTime
    #file = os.path.basename(__file__)


    cfg = {}

    def __init__(self, cfg):
        self.cfg = cfg
        self.hw_interface = self.cfg['interface']['name']
        self.hw_type = self.cfg['hw_type']
        print("c")

    def get_name(self): pass

    def init_com(self): pass

    def dbug_print(self, data):
        print(str(self.hw_type)+": "+data)

    def get_interface_type(self):
        return self.hw_type

    def get_hw_type(self):
        return self.hw_interface







