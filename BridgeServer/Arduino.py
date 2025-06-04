import serial

class ArduinoController:
    """Simple wrapper around ``serial.Serial`` used to communicate with the
    Arduino board.``serial.Serial`` may raise ``SerialException`` when the
    connection fails so we propagate a more descriptive ``ConnectionError``."""

    VALID_COMMANDS = {'1', '2', '3', '4'}

    def __init__(self, port, baud_rate, timeout=0.1):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.arduino = None

    def connect(self):
        """Connect to the Arduino if not already connected."""
        if self.arduino and self.arduino.is_open:
            return
        try:
            self.arduino = serial.Serial(
                port=self.port,
                baudrate=self.baud_rate,
                timeout=self.timeout,
            )
        except serial.SerialException as exc:  # pragma: no cover - hardware specific
            raise ConnectionError(f"Failed to connect to Arduino on {self.port}") from exc

    def disconnect(self):
        """Close the serial connection if it's open."""
        if self.arduino and self.arduino.is_open:
            self.arduino.close()

    def write_arduino(self, data):
        """Send a command to the Arduino.

        Parameters
        ----------
        data : str or int
            Should be one of ``1``-``4`` corresponding to a table.
        """
        if not self.arduino or not self.arduino.is_open:
            raise ConnectionError("Arduino is not connected")

        str_data = str(data)
        if str_data not in self.VALID_COMMANDS:
            raise ValueError(f"Invalid command: {data}")

        self.arduino.write(str_data.encode())
