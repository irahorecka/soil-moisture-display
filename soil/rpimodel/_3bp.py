import platform

# for development purposes (I always use MacOS)
if platform.system() == "Darwin":
    import FakeRPi.GPIO as GPIO
else:
    import RPi.GPIO as GPIO


class RPi_3BP:
    pi_model = "3B+"

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
        self._print_message(channel, 4)

    def _callback_5(self, channel):
        self._print_message(channel, 5)

    def _callback_6(self, channel):
        self._print_message(channel, 6)

    def _callback_12(self, channel):
        self._print_message(channel, 12)

    def _callback_13(self, channel):
        self._print_message(channel, 13)

    def _callback_16(self, channel):
        self._print_message(channel, 16)

    def _callback_17(self, channel):
        self._print_message(channel, 17)

    def _callback_18(self, channel):
        self._print_message(channel, 18)

    def _callback_19(self, channel):
        self._print_message(channel, 19)

    def _callback_20(self, channel):
        self._print_message(channel, 20)

    def _callback_21(self, channel):
        self._print_message(channel, 21)

    def _callback_22(self, channel):
        self._print_message(channel, 22)

    def _callback_23(self, channel):
        self._print_message(channel, 23)

    def _callback_24(self, channel):
        self._print_message(channel, 24)

    def _callback_25(self, channel):
        self._print_message(channel, 25)

    def _callback_26(self, channel):
        self._print_message(channel, 26)

    def _callback_27(self, channel):
        self._print_message(channel, 27)

    def _print_message(self, channel, gpio_pin):
        if GPIO.input(channel) or not GPIO.input(channel):
            print(f"{self.gpio_name_pair[gpio_pin]} is watered.")
