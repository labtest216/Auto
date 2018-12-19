import os
import sys
import time

import datetime
import schedule
import config as cfg

from datetime import datetime
from Utils.utils import get_class
#import RelayBoards.denkovi16






class Closet(object):
    # Get configuration data from file.
    #a=RelayBoards.denkovi16.Denkovi16(cfg.HW1["class_ctor"])


    hw_modules = {}
    grow_mode = True
    flower_mode = False

    def __init__(self):
        # Get all hw that connected to closet.
        self.get_hw_modules()
        # self.init_gpio()

    def get_hw_modules(self):
        i = 1
        while i <= cfg.Modules:

            # Get class dir file name.
            hw_module = getattr(cfg, "HW"+str(i))
            class_dir = hw_module["class_dir"]
            class_file = hw_module["class_file"]
            class_name = hw_module["class_name"]

            # Get constructor params.
            class_ctor = hw_module["class_ctor"]

            # Create class object.
            class_obj = get_class(class_dir+'.'+class_file+'.'+class_name)

            # Update HW modules with new hw module object instance.
            self.hw_modules[class_name] = class_obj(class_ctor)

            i += 1

    def water_on_timer(self, seconds):pass

    def set_water_on(self):
        print(str(datetime.now())+"set_water_on")

    def set_water_off(self):
        print(str(datetime.now())+"set_water_off")

    def set_led1_on(self):
        print(str(datetime.now())+"set_led_on")

    def set_led1_off(self):
        print(str(datetime.now()) + "set_led1_off")

    def set_fan_on(self):
        print(str(datetime.now()) + "set_fan_on")

    def set_fan_off(self):
        print(str(datetime.now())+"set_fan_of")

    def set_led2_off(self):
        rb = self.hw_modules[self.data["HW_M1"]["RelayBoard"]["sclass"]]
        rb.set_water_on()

    def get_sensors_samples(self):
        print("get_sensors_samples")

    def smart_watering(self):pass

    def start_program(self):
        start_flowering = self.grow_mode(self.data["GrowProgramStart"], self.data["GrowDays"])
        start_washing = self.flow_mode(start_flowering, self.data["FlowDays"])
        start_drying = self.wash_mode(start_washing, self.data["WashDays"])
        end_date = self.dry_mode(start_drying, self.data["DryDays"])
        return end_date

    def mode_pending(self,start_date, days):
        while True:
            if self.is_mode_finish(start_date, days) == True:
                schedule.clear()
                return self.date_time()
            elif self.is_mode_finish(start_date, days) == -1:
                print("waiting")
                pass
            else:
                schedule.run_pending()

    def grow_mode(self, start_date, days):
        print("grow mode start")
        schedule.every(3).seconds.do(self.get_sensors_samples)
        schedule.every(1).seconds.do(self.set_water_on)
        schedule.every(1).seconds.do(self.set_water_off)
        return self.mode_pending(start_date, days)

    def flow_mode(self, start_date, days):
        print("flower mode start")
        schedule.every(3).seconds.do(self.get_sensors_samples)
        schedule.every(7).seconds.do(self.set_led1_on)
        schedule.every(7).seconds.do(self.set_led1_off)
        return self.mode_pending(start_date, days)

    def wash_mode(self, start_date, days):
        print("harvest mode start")
        schedule.every(1).seconds.do(self.get_sensors_samples)
        schedule.every(1).seconds.do(self.set_led1_off)
        return self.mode_pending(start_date, days)

    def dry_mode(self, start_date, days):
        print("dry mode start")
        schedule.every(2).seconds.do(self.get_sensors_samples)
        return self.mode_pending(start_date, days)


        # schedule.every(2).day.do(self.water_on())
        # schedule.every().day.at("20:00").do(self.set_water_on)
        # schedule.every().day.at("20:01").do(self.set_water_off)
        #schedule.every().hour.do(self.get_sensors_samples)

        #schedule.every().day.at(self.data["LedOn"]).do(self.set_led1_on)
        #schedule.every().day.at("6:00").do(self.set_fan_on)
        #schedule.every().day.at(self.data["LedOff"]).do(self.set_led1_off)
        #schedule.every().day.at("23:00").do(self.set_fan_off)








    def is_mode_finish(self, start_date, growing_days):
        assert growing_days > 0, "Negative growing days"
        time_delta = datetime.now() - datetime(start_date["Y"], start_date["M"], start_date["D"])

        days = str(time_delta).find("days")
        day = str(time_delta).find("day,")

        if day == -1 and days > 0:  # -123 days or 123 days for example.
            passed_days = str(time_delta)[0:days - 1]
            if int(passed_days) < 0:  # Waiting to start mode.
                return -1
            elif int(passed_days) > 0:
                if int(passed_days) > int(growing_days):
                    return True  # End of mode.
                else:
                    return False  # Stay on this mode.
            else:
                print("Unknown state")
        elif day > 0 and days == -1:  # -1 day or 1 day for example.
            passed_days = str(time_delta)[0:day - 1]
            if int(passed_days) < 0:  # Waiting to start mode.
                return -1
            elif int(passed_days) > 0:
                if int(passed_days) > int(growing_days):
                    return True  # End of mode.
                else:
                    return False  # Stay on this mode.
        elif day == -1 and days == -1:  # start on end of day
            return -1
        else:
            print("Unknown state")


    def date_time(self):
        t = {"Y": int(datetime.now().date().year),
             "M": int(datetime.now().date().month),
             "D": int(datetime.now().date().day)}
        return t
    