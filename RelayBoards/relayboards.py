#!/usr/bin/python3
from HwModule.hw_modules import HwM


class RelayBoard(HwM):

    def __init__(self, cfg):
        super().__init__(cfg)
        self.hw_name = cfg["hw_name"]
        self.num_of_relay = cfg["num_of_relay"]

    def init_board(self): pass

    def set_switch(self, switch_num, mode): pass

    def send_and_wait(data_to_send, data_to_get): pass