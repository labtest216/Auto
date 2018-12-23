#!/usr/bin/python3
import Adafruit_BBIO.ADC as ADC
from Sensors.sensors import Sensor



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
