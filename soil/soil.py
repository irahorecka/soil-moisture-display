from .rpimodel import RPi_3BP
import platform

# for development purposes (I always use MacOS)
if platform.system() == "Darwin":
    import FakeRPi.GPIO as GPIO
else:
    import RPi.GPIO as GPIO


class Soil(RPi_3BP):
    # cannot inherit GPIO, as it is a class instance
    def __init__(self, gpio_map):
        super().__init__()
        if not isinstance(gpio_map, dict):
            raise TypeError("Expected <dict> argument.")
        for gpio_pin in gpio_map:
            if gpio_pin not in self.gpio_name_pair:
                raise KeyError(
                    f"{gpio_pin} is not a valid GPIO pin in Raspberry Pi model {self.pi_model}."
                )
            self.gpio_name_pair[gpio_pin] = gpio_map[gpio_pin]
        self._set_registered_gpio()

    def __setitem__(self, gpio_pin, name):
        if isinstance(gpio_pin, int) and gpio_pin in self.callback:
            self.gpio_name_pair[gpio_pin] = name
            self._set_registered_gpio()

    def __delitem__(self, gpio_pin):
        if isinstance(gpio_pin, int) and self.gpio_name_pair.get(gpio_pin):
            del self.gpio_name_pair[gpio_pin]
            self._set_registered_gpio()

    def __getitem__(self, gpio_pin):
        return self.gpio_name_pair.get(gpio_pin)

    def setup(self):
        self._setmode_gpio()
        self._setup_gpio_in()
        self._add_event_detect()
        self._add_event_callback()

    @staticmethod
    def _setmode_gpio():
        GPIO.setmode(GPIO.BCM)

    def _setup_gpio_in(self):
        for gpio_pin in self.registered_gpio:
            GPIO.setup(gpio_pin, GPIO.IN)

    def _add_event_detect(self):
        for gpio_pin in self.registered_gpio:
            GPIO.add_event_detect(gpio_pin, GPIO.BOTH, bouncetime=300)

    def _add_event_callback(self):
        for gpio_pin in self.registered_gpio:
            GPIO.add_event_callback(gpio_pin, self.callback[gpio_pin])

    def _set_registered_gpio(self):
        self.registered_gpio = [
            gpio for gpio, name in self.gpio_name_pair.items() if name
        ]
