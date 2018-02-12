#pulled from https://github.com/adafruit/Adafruit_Python_LSM303/blob/master/Adafruit_LSM303/LSM303.py

#libraries
import Adafruit_GPIO.I2C as I2C
import struct

class LSM303(object):

    def __init__(self, hires=True, accel_address=self.LSM303_ADDRESS_ACCEL, mag_address=self.LSM303_ADDRESS_MAG, **kwargs):
            #Constants carried over from Arduino library:
        self.LSM303_ADDRESS_ACCEL = (0x32 >> 1)  # 0011001x
        self.LSM303_ADDRESS_MAG   = (0x3C >> 1)  # 0011110x
                                         # Default    Type
        self.LSM303_REGISTER_ACCEL_CTRL_REG1_A = 0x20 # 00000111   rw
        self.LSM303_REGISTER_ACCEL_CTRL_REG4_A = 0x23 # 00000000   rw
        self.LSM303_REGISTER_ACCEL_OUT_X_L_A   = 0x28
        self.LSM303_REGISTER_MAG_CRB_REG_M     = 0x01
        self.LSM303_REGISTER_MAG_MR_REG_M      = 0x02
        self.LSM303_REGISTER_MAG_OUT_X_H_M     = 0x03

        self._accel = i2c.get_i2c_device(accel_address, **kwargs)
        self._mag = i2c.get_i2c_device(mag_address, **kwargs)
        self._accel.write8(self.LSM303_REGISTER_ACCEL_CTRL_REG1_A, 0x27)

        if hires:  #indicates if high resolution (12-bit) mode vs. low resolution (10-bit, faster and lower power) mode should be used.
            self._accel.write8(self.LSM303_REGISTER_ACCEL_CTRL_REG4_A, 0b00001000)
        else:
            self._accel.write8(self.LSM303_REGISTER_ACCEL_CTRL_REG4_A, 0)

        self._mag.write8(self.LSM303_REGISTER_MAG_MR_REG_M, 0x00)

    def read(self):
        # Read the accelerometer as signed 16-bit little endian values.
        accel_raw = self._accel.readList(self.LSM303_REGISTER_ACCEL_OUT_X_L_A | 0x80, 6)
        accel = struct.unpack('<hhh', accel_raw)
        # Convert to 12-bit values by shifting unused bits.
        accel = (accel[0] >> 4, accel[1] >> 4, accel[2] >> 4)
        # Read magnetometer:
        mag_raw = self._mag.readList(self.LSM303_REGISTER_MAG_OUT_X_H_M, 6)
        mag = struct.unpack('>hhh', mag_raw)
        return (accel, mag)

    def set_mag_gain(self,gain=self.LSM303_MAGGAIN_1_3):
        
        # Gain settings for set_mag_gain()
        self.LSM303_MAGGAIN_1_3 = 0x20 # +/- 1.3
        self.LSM303_MAGGAIN_1_9 = 0x40 # +/- 1.9
        self.LSM303_MAGGAIN_2_5 = 0x60 # +/- 2.5
        self.LSM303_MAGGAIN_4_0 = 0x80 # +/- 4.0
        self.LSM303_MAGGAIN_4_7 = 0xA0 # +/- 4.7
        self.LSM303_MAGGAIN_5_6 = 0xC0 # +/- 5.6
        self.LSM303_MAGGAIN_8_1 = 0xE0 # +/- 8.1

        self._mag.write8(self.LSM303_REGISTER_MAG_CRB_REG_M, gain)

if __name__ == '__main__':
    try:
        accelmag = LSM303()
        while True:
            AMdata = accelmag.read()
            print ("Read data = %.1f " % accelmag)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()