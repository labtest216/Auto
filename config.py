
GrowProgramStart = {"D": 26, "M": 11, "Y": 2018}
GrowDays = 3
FlowDays = 1
WashDays = 1
DryDays = 1

WiringMap = {
    "AIN4": "P9_33",
    "AIN6": "P9_35",
    "AIN5": "P9_36",
    "AIN2": "P9_37",
    "AIN3": "P9_38",
    "AIN0": "P9_39",
    "AIN1": "P9_40"
}

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
        "hw_name": "Max44009",
        "interface": {"name": "I2C", "com": "0x4a"},
        "units": "lux"
    }
}

HW3 = {
    "class_dir": "Sensors",
    "class_file": "bme250",
    "class_name": "Bme250",
    "class_ctor": {
        "hw_type": "THPSensor",
        "hw_name": "Bme250",
        "interface": {"name": "I2C", "com": "0x7a"},
        "units": {"t": "c", "h": "%", "p": "pas"}
    }
}

HW4 = {
    "class_dir": "Sensors",
    "class_file": "bme250",
    "class_name": "Bme250",
    "class_ctor": {
        "hw_type": "SoilSensor",
        "hw_name": "yl-69_left",
        "interface": {"name": "AIN0", "com": "P9_39", "ref_voltage": 1.8},
        "units": "Volt"
    }
}

HW5 = {
    "class_dir": "Sensors",
    "class_file": "yl-69",
    "class_name": "Yl-69",
    "class_ctor": {
        "hw_type": "SoilSensor",
        "hw_name": "yl-69_right",
        "interface": {"Name": "AIN1", "Com": "P9_40", "ref_voltage": 1.8},
        "hw_pins": {"vcc":"3.3-5v","gnd":"gnd","Do":"P9_41","Ao":"P9_42"},
        "units": "Volt"
    }
}

HW6 = {
    "class_dir": "Sensors",
    "class_file": "water_level",
    "class_name": "WaterLevel",
    "class_ctor": {
        "hw_type": "WaterLevelSensor",
        "hw_name": "waterLevSens",
        "interface": {"Name": "GPIO", "Com": "P9_40,P9_41,P9_42", "ref_voltage": 1.8},
        "hw_pins": {"vcc":"3.3v","gnd":"gnd","p1":"P9_41","p2":"P9_42","p3":"P9_43"},
        "units": "Level"
    }
}

HW7 = {
    "class_dir": "Sensors",
    "class_file": "yy6237",
    "class_name": "Yy6237",
    "class_ctor": {
        "hw_type": "PhSensor",
        "hw_name": "Yy6237",
        "interface": {"Name": "AIN1", "Com": "P9_40", "ref_voltage": 1.8},
        "hw_pins": {"vcc":"3.3-5v","gnd":"gnd","Do":"P9_41","Ao":"P9_42"},
        "units": "Volt"
    }
}





