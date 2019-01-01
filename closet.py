import os
import sys
import time
import datetime
import schedule
import config as cfg

from datetime import datetime
from Utils.utils import get_class
#import RelayBoards.denkovi16

class Closet:

    hw_modules = {}
    grow_mode = True
    flower_mode = False
    samples = {}

    def __init__(self):

        # Get all hw that connected to closet.
        self.get_hw_modules()
        # Start growing program.
        self.start_program()

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

    def get_sensors_samples(self):
        for sensor in self.hw_modules:

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
    