from pybricks.iodevices  import I2CDevice

LSA_DEFAULT_ADDRESS         = const(0x14)
LSA_COMMAND                 = const(0x41)
LSA_CALIBRATED              = const(0x42)
LSA_UNCALIBRATED            = const(0x6A)
LSA_WHITE_LIMIT             = const(0x4A)
LSA_BLACK_LIMIT             = const(0x52)
LSA_WHITE_CALIBRATION_DATA  = const(0x5A)
LSA_BLACK_CALIBRATION_DATA  = const(0x62)

class LightSensorArray:
    device_address = 0

    def __init__(self, port):
        self.port = port
        self.device_addres = LSA_DEFAULT_ADDRESS
        self.i2c_device = I2CDevice(port, LSA_DEFAULT_ADDRESS>>1)

    def get_data(self, address, size) -> bytearray | None:
        try:
            data = self.i2c_device.read(address, size)
            return bytearray(data)

        except OSError:
            print("ERROR: falha na comunicação com o dispositivo I2C, verifique os cabos do sensor e a entrada correspondente.")

    def send_command(self, cmd) -> None:
        self.i2c_device.write(reg=LSA_COMMAND, data=cmd)

    def calibrate_white(self) -> None:
        self.send_command(b'W')

    def calibrate_black(self) -> None:
        self.send_command(b'B')

    def wakeup(self) -> None:
        self.send_command(b'P')

    def goto_sleep(self) -> None:
        self.command(b'D')

    def read_calibrated(self) -> bytearray | None:
        return self.get_data(LSA_CALIBRATED, 8)

    def get_raw_voltages(self) -> bytearray | None:
        s = self.get_data(LSA_UNCALIBRATED, 16)
        array = [ int(s[0:1]), s[2:3], s[4:5], s[6:7], s[8:9], s[10:11], s[12:13], s[14:15] ]
        return array

    def get_white_limit(self) -> bytearray | None:
        data = self.get_data(LSA_WHITE_LIMIT, 8)
        arr = [ data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7] ]
        return arr

    def get_black_limit(self) -> bytearray | None:
        data = self.get_data(LSA_BLACK_LIMIT, 8)
        arr = [ data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7] ]
        return arr

    def get_white_calibration_data(self) -> bytearray | None:
        data = self.get_data(LSA_WHITE_CALIBRATION_DATA, 8)
        arr = [ data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7] ]
        return arr

    def get_black_calibration_data(self) -> bytearray | None:
        data = self.get_data(LSA_BLACK_CALIBRATION_DATA, 8)
        arr = [ data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7] ]
        return arr