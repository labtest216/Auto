
GrowProgramStart = {"D": 26, "M": 11, "Y": 2018}
GrowDays = 3
FlowDays = 1
WashDays = 1
DryDays = 1

Modules = 4

HW1 = {
    "class_dir": "RelayBoards",
    "class_file": "denkovi16",
    "class_name": "Denkovi16",
    "class_ctor": {
        "hw_type": "RelayBoard",
        "hw_name": "Denkovi16",
        "num_of_relay": 16,
        "interface": {"name": "UART", "com": "/dev/ttyUSB0", "br": 9600},
        "led1": 1,
        "fan1": 2,
        "pump": {"SW": 3, "TimeOn": 10}
    }
}

HW2 = {
    "class_dir": "Sensors",
    "class_file": "max44009",
    "class_name": "Max44009",
    "class_ctor": {
        "hw_type": "LightSensor",
        "interface": {"name": "I2C", "com": "0x4a"},
        "Units": "lux"
    }
}

HW3 = {
    "class_dir": "Sensors",
    "class_file": "bme250",
    "class_name": "Bme250",
    "class_ctor": {
        "hw_type": "THPSensor",
        "Interface": {"Name": "I2C", "Com": "0x7a"},
        "Units": {"temp": "c", "hum": "%", "pressure": "pas"}
    }
}

HW4 = {
    "class_dir": "Sensors",
    "class_file": "bme250",
    "class_name": "Bme250",
    "class_ctor": {
        "hw_type": "SoilSensor",
        "Interface": {"Name": "AI", "Com": "0x7a"},
        "Units": "Volt"
    }
}





