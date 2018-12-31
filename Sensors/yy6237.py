#!/usr/bin/python3
#import Adafruit_BBIO.ADC as ADC
from Sensors.sensors import Sensor
from decimal import Decimal


class Yy6237(Sensor):
    """
    Sensor measure soil PH level.
    https://scidle.com/how-to-use-a-ph-sensor-with-arduino/

    PH 14 acidity : the output voltage decreases down to 0v on Ao pin.
    PH 0 alkalinity: the output voltage increases up to 5v on Ao pin.
    Interrupt too much acidity : '1' logic 3.3v on pin Do.
    Interrupt too much alkalinity:'0' logic 0v on pin Do.
    """


    def __init__(self, cfg):
        super().__init__(cfg)
        self.set_calibration()
        self.add_interrupts()

    def set_calibration(self):
        self.dprint("not imp")

    def sample_format_display(self):
        return str(self.sample)+" "+self.cfg["units"]

    def get_sample(self):
        ADC.setup()
        self.sample = ADC.read(self.interface["com"])
        self.dprint(self.sample_format_display())
        return self.sample

    def get_avg_sample(self, num_of_samples=None):

        if num_of_samples is None:
            num_of_samples = 3

        samples = [num_of_samples]
        for sample in samples:
            value = self.get_sample()
            samples[sample] = value
        self.sample = sum(samples)/len(samples)
        self.dprint(self.sample_format_display())
        return self.sample

    def add_interrupts(self):
        GPIO.add_event_detect(self.cfg["hw_pins"]["Do"], GPIO.FALLING, callback=self.ground_is_wet, bouncetime=300)
        GPIO.add_event_detect(self.cfg["hw_pins"]["Do"], GPIO.RISING, callback=self.ground_is_dry, bouncetime=300)

    def ground_is_wet(self):
        self.dprint(self.get_sample())
        return True

    def ground_is_dry(self):
        self.dprint(self.get_sample())
        return True



def set_ph(end_volt, res):

    ph_step = 14/res
    volt_step = end_volt/res

    ph_to_volt = []
    ph = 0
    volt = end_volt

    while ph <= 14:
        i = [round(Decimal(ph), 4), round(Decimal(volt), 4)]
        ph_to_volt.append(i)
        ph += ph_step
        volt -= volt_step

    return ph_to_volt

def get_ph_(ph_to_volt, volt):


    for i in range(0, len(ph_to_volt)):
        # ph_to_volt is list of list of ph vs volt.

        j = ph_to_volt[i]
        if volt < 0 or volt > j[1]:
            return -1
        elif volt >= j[1] and j[0] == 0:
            return j[0]  # Return ph 0.
        elif volt <= j[1] and j[0] == 14:
            return j[0]  # Return ph 14.
        elif volt <= j[1]:

            continue
        elif volt >= j[1]: #
            last_j = ph_to_volt[i-1]
            delta1 = Decimal(volt) - last_j[1]
            delta2 = j[1] - Decimal(volt)
            if delta1 > delta2:
                print("d1="+str(last_j[1]))
                return last_j[0]
            else:
                print("d1=" + str(last_j[1]))
                return j[0]
        else:
            return -1


def get_ph(ph_to_volt, volt):
    # ph_to_volt is list of list of ph vs volt.
    j = ph_to_volt[0]
    if volt < 0 or volt > j[1]:  # if volt not in ph vs volt table.
        return -1

    for i in range(0, len(ph_to_volt)):
        j = ph_to_volt[i]

        if volt < j[1]:
            continue

        elif volt >= j[1]:
            last_j = ph_to_volt[i-1]
            delta1 = Decimal(volt) - last_j[1]
            delta2 = j[1] - Decimal(volt)
            if delta1 > delta2:
                return last_j[0]
            else:
                return j[0]
        else:
            return -1





a=set_ph(1.42, 140000)

print(get_ph(a, 0.71))


