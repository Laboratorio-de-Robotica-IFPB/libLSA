from pybricks.iodevices import Ev3devSensor

# Using the Ev3devSensor's API:

class LSA(Ev3devSensor):

    def __init__(self, port):
        """Initialize the sensor."""

        # Initialize the parent class.
        super().__init__(port)

        # Get the sysfs path.
        self.path = '/sys/class/lego-sensor/sensor' + str(self.sensor_index)

    def get_modes(self):
        """Get a list of mode strings so we don't have to look them up."""

        # The path of the modes file.
        modes_path = self.path + '/modes'

        # Open the modes file.
        with open(modes_path, 'r') as m:

            # Read the contents.
            contents = m.read()

            # Strip the newline symbol, and split at every space symbol.
            return contents.strip().split(' ')    

    def calibrate_white(self):
        # TODO
        pass

    def calibrate_black(self):
        # TODO
        pass

    def read_calibrated(self):
        return self.read('CAL')

    def read_raw(self):
        return self.read('RAW')
