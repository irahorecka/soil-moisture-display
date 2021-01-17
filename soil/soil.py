from .rpimodel import RPi_3BP
import platform

# for development purposes (I always use MacOS)
if platform.system() == "Darwin":
    import FakeRPi.GPIO as GPIO
else:
    import RPi.GPIO as GPIO


class Soil(RPi_3BP):
    # cannot inherit GPIO, as it is a class instance
    def __init__(self, gpio_mapping):
        super().__init__()
        if not isinstance(gpio_mapping, dict):
            raise TypeError("Expected <dict> argument.")
        for gpio_pin, plant in gpio_mapping.items():
            if gpio_pin not in self.gpio_name_pair:
                raise KeyError(
                    f"{gpio_pin} is not a valid GPIO pin in Raspberry Pi model 3B+."
                )
            self.gpio_name_pair[gpio_pin] = gpio_mapping[gpio_pin]

    def __setitem__(self, gpio_pin, name):
        if isinstance(gpio_pin, int) and gpio_pin in self.callback:
            self.gpio_name_pair[gpio_pin] = name

    def __delitem__(self, gpio_pin):
        if isinstance(gpio_pin, int) and self.gpio_name_pair.get(gpio_pin):
            del self.gpio_name_pair[gpio_pin]

    def __getitem__(self, gpio_pin):
        return self.gpio_name_pair.get(gpio_pin)

    def setup(self, bouncetime=100):
        self._setmode_gpio()
        self._setup_gpio_in()
        self._add_event_detect(bouncetime=bouncetime)
        self._add_event_callback()

    @staticmethod
    def _setmode_gpio():
        GPIO.setmode(GPIO.BCM)

    def _setup_gpio_in(self):
        for key in self.gpio_name_pair:
            GPIO.setup(key, GPIO.IN)

    def _add_event_detect(self, bouncetime):
        for key in self.gpio_name_pair:
            GPIO.add_event_detect(key, GPIO.BOTH, bouncetime=bouncetime)

    def _add_event_callback(self):
        for gpio_pin in self.gpio_name_pair:
            GPIO.add_event_callback(gpio_pin, self.callback[gpio_pin])
