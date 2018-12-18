from HwModule.hw_modules import HwModule


class RelayBoard(HwModule):
    """Base class for switches card."""

    def __int__(self, cfg):
        super().__init__(self, cfg)
        self.cfg = cfg
        self.sw_num = cfg["sw_num"]
        print("b")


    def init_com(self): pass

    def set_switch(self, switch_num, mode): pass

    def set_water_on(self):
        self.set_switch(self.cfg["Connections"]["waterpump_switch"]["sw"], 1)

    def set_water_off(self):
        self.set_switch(self.cfg["waterpump_switch"], 0)



