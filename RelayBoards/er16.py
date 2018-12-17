#!/usr/bin/python3
from HwModule.hw_modules import RelayBoard


class ER16(RelayBoard):

    num_of_relay = 16
    board_name = "ER16"
    all_switches_off = "off//"
    relay_card_test = "ask//"
    switches_off = {"1": "01", "2": "02-//", "3": "03-//", "4": "04-//", "5": "05-//", "6": "06-//", "7": "07-//", "8": "08-//", "9": "09-//", "10": "10-//", "11": "11-//", "12": "12-//", "13": "13-//", "14": "14-//", "15": "15-//", "16": "16-//"}
    switches_on = {"1": "01+//", "2": "02+//", "3": "03+//", "4": "04+//", "5": "05+//", "6": "06+//", "7": "07+//", "8": "08+//", "9": "09+//", "10": "10+//", "11": "11+//", "12": "12+//", "13": "13+//", "14": "14+//", "15": "15+//", "16": "16+//"}

    def init_com(self):
        self.com = Serial(self.cfg["Interface"]["comName"], self.cfg["Interface"]["baudRate"], 8, 'N', 1)
        if self.com.is_open:
            dprint("Communication with relay board open.")
            self.init_relay_card()
        else:
            dprint("Com can not open, Communication with relay board fail.")

    def init_board(self):
        if self.send_and_wait(self.all_switches_off, "off") == 0:
            if self.send_and_wait(self.relay_card_test, "\x00\x00") == 0:
                u.dprint(u.f_name() + " pass")
                return 0
            else:
                u.dprint(u.f_name() + " fail")
                return -1
        else:
            u.dprint(u.f_name() + " fail")
            return -1
            # Switch On =1, Switch Off=0 .

    def set_switch(self, switch_num, mode):
        assert 1 <= switch_num <= 16, " No switch like this"
        if mode == 1:  # Switch On.
            feedback = self.switches_on[str(switch_num)]
            if self.send_and_wait(self.switches_on[str(switch_num)], feedback) == 0:
                u.dprint(u.f_name() + " number " + str(switch_num) + " on pass")
                return 0
            else:
                u.dprint(u.f_name() + " fail")
                return -1