from . import lcd


class BaseRPi:
    """ Base class to be inherited by children RPi models. """

    def __init__(self):
        # To be inherited and modified by children class
        self.gpio_name_pair = {}

    def display_moisture(self, *args, **kwargs):
        """ Display moisture readout on different media. """
        # Unpack *arg, must be only GPIO channel, display medium, and
        # moisture bool. The reason for *arg unpacking is due to the higher-order
        # property of GPIO.add_event_callback
        channel, display_medium, is_moist = args
        if display_medium == "lcd":
            lcd.display(
                self.gpio_name_pair[channel], "is watered.", **kwargs
            ) if is_moist else lcd.display(
                self.gpio_name_pair[channel], "needs water.", **kwargs
            )
