#!/usr/bin/python3

import time
import smbus
from Sensors.sensors import Sensor
from Utils.utils import dprint, f_name


class Max44009(Sensor):
    """
        Sensor measure light level.

        """

    def __init__(self, cfg):
        super().__init__(cfg)
        self.set_calibration()

    def set_calibration(self):
        dprint(f_name() + "not imp")

    def get_sample(self):
        ic2_addr = self.interface["com"]
        # Get I2C bus
        bus = smbus.SMBus(1)

        # MAX44009 address, 0x4A(74)
        # Select configuration register, 0x02(02)
        # 0x40(64)	Continuous mode, Integration time = 800 ms
        bus.write_byte_data(ic2_addr, 0x02, 0x40)

        time.sleep(0.5)

        # MAX44009 address, 0x4A(74)
        # Read data back from 0x03(03), 2 bytes
        # luminance MSB, luminance LSB
        data = bus.read_i2c_block_data(ic2_addr, 0x03, 2)

        # Convert the data to lux
        exponent = (data[0] & 0xF0) >> 4
        mantissa = ((data[0] & 0x0F) << 4) | (data[1] & 0x0F)
        luminance = ((2 ** exponent) * mantissa) * 0.045

        # Output data to screen
        dprint(f_name() + "Ambient Light luminance : %.2f" + self.cfg["units"] % luminance)
        return luminance