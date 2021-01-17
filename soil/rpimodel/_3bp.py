import platform

# for development purposes (I always use MacOS)
if platform.system() == "Darwin":
    import FakeRPi.GPIO as GPIO
else:
    import RPi.GPIO as GPIO


class RPi_3BP:
    def __init__(self):
        self.gpio_name_pair = {
            4: "",
            5: "",
            6: "",
            12: "",
            13: "",
            16: "",
            17: "",
            18: "",
            19: "",
            20: "",
            21: "",
            22: "",
            23: "",
            24: "",
            25: "",
            26: "",
            27: "",
        }
        self.callback = {
            4: self._callback_4,
            5: self._callback_5,
            6: self._callback_6,
            12: self._callback_12,
            13: self._callback_13,
            16: self._callback_16,
            17: self._callback_17,
            18: self._callback_18,
            19: self._callback_19,
            20: self._callback_20,
            21: self._callback_21,
            22: self._callback_22,
            23: self._callback_23,
            24: self._callback_24,
            25: self._callback_25,
            26: self._callback_26,
            27: self._callback_27,
        }

    def _callback_4(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[4]} is fine.")

    def _callback_5(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[5]} is fine.")

    def _callback_6(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[6]} is fine.")

    def _callback_12(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[12]} is fine.")

    def _callback_13(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[13]} is fine.")

    def _callback_16(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[16]} is fine.")

    def _callback_17(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[17]} is fine.")

    def _callback_18(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[18]} is fine.")

    def _callback_19(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[19]} is fine.")

    def _callback_20(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[20]} is fine.")

    def _callback_21(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[21]} is fine.")

    def _callback_22(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[22]} is fine.")

    def _callback_23(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[23]} is fine.")

    def _callback_24(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[24]} is fine.")

    def _callback_25(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[25]} is fine.")

    def _callback_26(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[26]} is fine.")

    def _callback_27(self, channel):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[27]} is fine.")
