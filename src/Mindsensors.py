from pybricks.iodevices  import I2CDevice
from micropython import const

LSA_DEFAULT_ADDRESS         = const(0x14)
LSA_COMMAND                 = const(0x41)
LSA_CALIBRATED              = const(0x42)
LSA_UNCALIBRATED            = const(0x6A)
LSA_WHITE_LIMIT             = const(0x4A)
LSA_BLACK_LIMIT             = const(0x52)
LSA_WHITE_CALIBRATION_DATA  = const(0x5A)
LSA_BLACK_CALIBRATION_DATA  = const(0x62)

class LightSensorArray:
    def __init__(self, port):
        self.port = port
        self.device_addres = LSA_DEFAULT_ADDRESS
        self.i2c_device = I2CDevice(port, LSA_DEFAULT_ADDRESS>>1)

    def get_data(self, address, size) -> bytearray | None:
        try:
            data = self.i2c_device.read(address, size)
            return bytearray(data)

        except OSError:
            print("ERROR: Failed to communicate with the I2C device. Please check the sensor cables and the corresponding input port.")

    def send_command(self, cmd) -> None:
        self.i2c_device.write(reg=LSA_COMMAND, data=cmd)

    def calibrate_white(self) -> None:
        self.send_command(b'W')

    def calibrate_black(self) -> None:
        self.send_command(b'B')

    # TODO: needs testing
    def wakeup(self) -> None:
        self.send_command(b'P')

    # TODO: needs testing
    def sleep(self) -> None:
        self.command(b'D')

    def read_calibrated(self) -> list | None:
        return [ x for x in self.get_data(LSA_CALIBRATED, 8)]

    # TODO: select the valid elements for reading the raw voltage of each sensor 
    # apparently, the odd indexes are always 0 
    def read_raw(self) -> list | None:
        return [x for x in self.get_data(LSA_UNCALIBRATED, 16)]

    def get_white_limit(self) -> list | None: 
        return [x for x in self.get_data(LSA_WHITE_LIMIT, 8)]

    def get_black_limit(self) -> list | None:
        return [x for x in self.get_data(LSA_BLACK_LIMIT, 8)]

    def get_white_calibration_data(self) -> list | None:
        return [x for x in self.get_data(LSA_WHITE_CALIBRATION_DATA, 8)]

    def get_black_calibration_data(self) -> list | None:
        return [x for x in self.get_data(LSA_BLACK_CALIBRATION_DATA, 8)]