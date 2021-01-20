from . import lcd
import platform
import sys

# for development purposes (I always use MacOS)
if platform.system() == "Darwin":
    import fake_rpi

    sys.modules["RPi"] = fake_rpi.RPi
    sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO
import RPi.GPIO as GPIO


class BaseRPi:
    """ Base class to be inherited by children RPi models. """

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        # To be inherited and modified by children class
        self.gpio_name_pair = {}
        self.callback_method = {}
        self.display_medium = ""

    def display_moisture(self, channel, **kwargs):
        """ Display moisture readout on different media. """
        # Unpack *arg, must be only GPIO channel, display medium, and
        # moisture bool. The reason for *arg unpacking is due to the higher-order
        # property of GPIO.add_event_callback
        if self.display_medium == "lcd":
            lcd.display(
                self.gpio_name_pair[channel], "is watered.", **kwargs
            ) if self._is_moist(channel) else lcd.display(
                self.gpio_name_pair[channel], "needs water.", **kwargs
            )

    @staticmethod
    def _is_moist(gpio_channel):
        return bool(GPIO.input(gpio_channel) == GPIO.LOW)

    @staticmethod
    def gpio_setup(*args, **kwargs):
        """ Provide class interface for GPIO.setup """
        mode = kwargs.get("mode")
        if mode == "in":
            GPIO.setup(*args, GPIO.IN)
        elif mode == "out":
            GPIO.setup(*args, GPIO.OUT)
        else:
            raise ValueError(f"{mode} is not an acceptable keyword argument.")

    @staticmethod
    def gpio_add_event_detect(gpio_channel, **kwargs):
        """ Provide class interface for GPIO.add_event_detect """
        GPIO.add_event_detect(gpio_channel, GPIO.BOTH, **kwargs)

    def gpio_add_event_callback(self, channel):
        """ Provide class interface for GPIO.add_event_callback """
        GPIO.add_event_callback(channel, self.callback_method[channel])

    @staticmethod
    def gpio_cleanup(*args, **kwargs):
        """ Provide class interface for GPIO.cleanup """
        GPIO.cleanup(*args, **kwargs)
