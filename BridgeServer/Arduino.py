import serial

class ArduinoController:
    def __init__(self, port, baud_rate):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = .1
        self.arduino = None

    def connect(self):
        self.arduino = serial.Serial(port=self.port, baudrate=self.baud_rate, timeout=self.timeout)

    def write_arduino(self, data):
        if data in ['1', '2', '3', '4']:
            self.arduino.write(data.encode())