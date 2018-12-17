


import json
import os
import configparser
import time
from datetime import datetime
#import datetime
import schedule
import Auto.



#from RelayBoards.denkovi16 import Denkovi16


from Utils.utils import get_class




class Closet(object):
    # Get configuration data from file.
    script_dir = str(os.path.dirname(os.path.realpath(__file__)))
    config_file = open(str(script_dir+"/config.json"), "r+")
    data = configparser.Config
    # Get modules numbers.
    hm_num = data['Modules']
    hw_modules = {}
    smart_watering_fleg = data["smart_water"]
    grow_mode = True
    flower_mode = False


    def __init__(self):
        # Get all hw that connected to closet.
        self.get_hw_modules()
        # self.init_gpio()

    def get_hw_modules(self):
        i = 1
        while i <= self.hm_num:
            data = self.data


            # Get base class and sub class names.
            bclass = data["HW_M" + str(i)]["bclass"]
            sclass = data["HW_M" + str(i)][bclass]["sclass"]
#            dir = data["HW_M" + str(i)]["dir"]
            file = data["HW_M" + str(i)]["file"]
            # Get constructor params for relay board.
            cfg = data["HW_M" + str(i)][bclass][sclass]


            # Create object.
            class_obj = get_class("RelayBoards.denkovi16.Denkovi16")



            # Update HW modules with new hw module object instance.
#            self.hw_modules[sclass] = class_obj(cfg)

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
    