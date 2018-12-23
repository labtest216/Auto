#!/usr/bin/python3

import time
import smbus
from Sensors.sensors import Sensor


class Bme280(Sensor):
    """
            Sensor measure temperature,humidity and pressure level.

            """
    def __init__(self, cfg):
        super().__init__(cfg)
        self.set_calibration()

    def set_calibration(self):
        self.dprint("not imp")

    def get_sample(self):
        ic2_addr = self.interface["com"]
        # Get I2C bus
        bus = smbus.SMBus(1)

        # BME280 address, 0x4A(74)
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
        thp = ((2 ** exponent) * mantissa) * 0.045

        # Output data to screen
        self.dprint("temperature humidity pressure : %.2f"+self.cfg["units"] % thp)
        return thp

    xDevs.com
    Python
    10
    V
    test
    for 3458A
    # http://xdevs.com/guide/ni_gpib_rpi/
    import os.path
    import sys
    import Gpib
    import time
    import ftplib
    import numbers
    import signal
    from Adafruit_BME280 import *

    root_dir = '/repo/3458/'
    fileName4 = root_dir + '2v5_3458_nplc200_tin_00000.csv'

    cnt = 0
    tread = 20
    reflevel = 2.5000000

    exttemp = 25.0
    rh = 50.0
    pascals = 100000.00
    hectopascals = 1000.00

    class Timeout():
        """Timeout class using ALARM signal"""

        class Timeout(Exception): pass

        def __init__(self, sec):
            self.sec = sec

        def __enter__(self):
            signal.signal(signal.SIGALRM, self.raise_timeout)
            signal.alarm(self.sec)

        def __exit__(self, *args):
            signal.alarm(0)  # disable alarm

        def raise_timeout(self, *args):
            raise Timeout.Timeout()

    class meter():
        temp = 38.5
        data = ""
        ppm = 0.0
        status_flag = 1
        temp_status_flag = 1
        global exttemp
        global rh
        global hectopascals

        def __init__(self, gpib, reflevel, name):
            self.gpib = gpib
            self.inst = Gpib.Gpib(0, self.gpib, timeout=60)  # 3458A GPIB Address = self.gpib
            self.reflevel = reflevel
            self.name = name
            self.init_inst()

        def init_inst(self):
            # Setup HP 3458A
            self.inst.clear()
            self.inst.write("PRESET NORM")
            self.inst.write("OFORMAT ASCII")
            self.inst.write("DCV 10")
            self.inst.write("TARM HOLD")
            self.inst.write("TRIG AUTO")
            self.inst.write("NPLC 200")
            self.inst.write("AZERO ON")
            self.inst.write("LFILTER ON")
            self.inst.write("NRDGS 1,AUTO")
            self.inst.write("MEM OFF")
            self.inst.write("END ALWAYS")
            self.inst.write("NDIG 9")

        def read_data(self, cmd):
            data_float = 0.0
            data_str = ""
            self.inst.write(cmd)
            try:
                with Timeout(20):
                    data_str = self.inst.read()
            except Timeout.Timeout:
                print("Timeout exception from dmm %s on read_data() inst.read()\n" % self.name)
                return (0, float(0))
            # print ("Reading from dmm %s = %s" % (self.name,data_str))
            try:
                data_float = float(data_str)
            except ValueError:
                print("Exception thrown by dmm %s on read_data() - ValueError = %s\n" % (self.name, data_str))
                return (0, float(0))  # Exception on float conversion, 0 = error
            return (1, data_float)  # Good read, 1 = converted to float w/o exception

        def get_temp(self):
            self.inst.write("TARM SGL,1")
            self.temp_status_flag, temp = self.read_data("TEMP?")
            if (self.temp_status_flag):
                self.temp = temp
            return self.temp

        def get_temp_status(self):
            return self.temp_status_flag

        def get_data(self):
            self.status_flag, data = self.read_data("TARM SGL,1")
            if (self.status_flag):
                self.data = data
                self.ppm = ((float(self.data) / self.reflevel) - 1) * 1E6
            return self.data

        def get_data_status(self):
            return self.status_flag

        def write_data(self, fileHandle):
            print
            time.strftime("%d/%m/%Y-%H:%M:%S;") + (
                        "[%8d]: %2.9f , dev %4.4f ppm, T:%3.1f , EXT_T:%3.2f , RH:%3.2f , Press:%4.2f hPa" % (
                cnt, float(self.data), float(self.ppm), float(self.temp), float(exttemp), float(rh),
                float(hectopascals)))
            fileHandle.write(time.strftime("%d/%m/%Y-%H:%M:%S;") + (
                        "%16.8f;%16.8f;%3.1f;%4.3f;%3.2f;%3.2f;%4.2f;\r\n" % (
                float(self.data), float(self.reflevel), float(self.temp), float(self.ppm), float(exttemp), float(rh),
                float(hectopascals))))

        def print_ppm(self):
            self.inst.write("DISP OFF, \"%3.3f ppm\"" % float(self.ppm))

    # Read Temperature, Humidity, and Barometric Pressure from BME280
    def get_THP():
        global exttemp
        global rh
        global pascals
        global hectopascals
        exttemp = sensor.read_temperature()
        rh = sensor.read_humidity()
        pascals = sensor.read_pressure()
        hectopascals = pascals / 100

    # Check if file exists, if not create it and add header
    def create_local_file(fileName):
        if (os.path.isfile(fileName) == False):
            with open(fileName, 'a') as o:
                o.write("date;hp3458a;level;temp;ppm_level;ext_temp;rh;pressure;\r\n")
                print("file %s does not exist\r\n" % fileName)
        else:
            print("file %s exists\r\n" % fileName)

    meter1 = meter(3, reflevel, "3458A_00000")  # Gpib 3

    gen = Gpib.Gpib(0, 2, timeout=60)  # 3245A GPIB Address
    gen.clear()
    gen.write("DISP MSG,\"            \"")
    gen.write("DISP ON")

    meter1.get_temp()

    # Setup temp/humidity/pressure sensor BME280
    # OSAMPLE = oversampling mode
    sensor = BME280(mode=BME280_OSAMPLE_8)
    get_THP()  # Read Temp, RH, Pressure from sensor

    # Create file for 1st 3458A and write header if needed
    create_local_file(fileName4)

    while cnt <= 10000000:
        cnt += 1
        with open(fileName4, 'a') as o1:  # Open file handles for file
            tread = tread - 1
            if (tread == 0):
                tread = 20
                meter1.get_temp()

            get_THP()  # Read Temp, RH, Press from sensor
            meter1.get_data()
            if (meter1.get_data_status()):
                meter1.print_ppm()
                meter1.write_data(o1)

            o1.close()



