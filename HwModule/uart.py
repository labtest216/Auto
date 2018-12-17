def __init__(self):
    self.com = serial.Serial(self.rb.com_name, baudrate=self.rb.baud_rate, self.rb.byte_size, parity='N',
                             self.rb.stop_bits, self.rb.time_out)

    if self.com.is_open:
        dprint("Comunication with relay board open.")
        self.init_relay_card()
    else:
        dprint("Com can not open, Communication with relay board fail.")