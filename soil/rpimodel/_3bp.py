from .base import BaseRPi


class RPi_3BP(BaseRPi):
    pi_model = "3B+"

    def __init__(self):
        super().__init__()
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
        self.callback_method = {
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

    def _callback_4(self, *args):
        self.display_moisture(*args)

    def _callback_5(self, *args):
        self.display_moisture(*args)

    def _callback_6(self, *args):
        self.display_moisture(*args)

    def _callback_12(self, *args):
        self.display_moisture(*args)

    def _callback_13(self, *args):
        self.display_moisture(*args)

    def _callback_16(self, *args):
        self.display_moisture(*args)

    def _callback_17(self, *args):
        self.display_moisture(*args)

    def _callback_18(self, *args):
        self.display_moisture(*args)

    def _callback_19(self, *args):
        self.display_moisture(*args)

    def _callback_20(self, *args):
        self.display_moisture(*args)

    def _callback_21(self, *args):
        self.display_moisture(*args)

    def _callback_22(self, *args):
        self.display_moisture(*args)

    def _callback_23(self, *args):
        self.display_moisture(*args)

    def _callback_24(self, *args):
        self.display_moisture(*args)

    def _callback_25(self, *args):
        self.display_moisture(*args)

    def _callback_26(self, *args):
        self.display_moisture(*args)

    def _callback_27(self, *args):
        self.display_moisture(*args)
