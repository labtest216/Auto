from RelayBoards.relayboards import Denkovi16, ER16
from Sensors.sensors import BME250, MAX44009


class HwFactory(object):

    def factory(type):
        if type == "Denkovi16":
            return Denkovi16()
        if type == "ER16":
            return ER16()
        if type == "MAX44009":
            return MAX44009()
        if type == "BME250":
            return BME250()
        assert -1, "Bad hw module creation: " + type

    factory = staticmethod(factory)

# Create object using factory.
#obj = Car.factory("Racecar")
#obj.drive()