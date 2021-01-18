from .rpimodel import RPi_3BP
import platform
import sys
import time

# for development purposes (I always use MacOS)
if platform.system() == "Darwin":
    import fake_rpi

    sys.modules["RPi"] = fake_rpi.RPi
    sys.modules["RPi.GPIO"] = fake_rpi.RPi.GPIO
import RPi.GPIO as GPIO


class Soil(RPi_3BP):
    """ Simple API to hook up and detect soil moisture hardware to your
    Raspberry Pi. """

    def __init__(self, gpio_map):
        GPIO.setmode(GPIO.BCM)
        super().__init__()
        if not isinstance(gpio_map, dict):
            raise TypeError("Expected <dict> argument.")
        self._register_gpio(gpio_map)

    def __setitem__(self, gpio_channel, name):
        if isinstance(gpio_channel, int) and gpio_channel in self.callback:
            self.gpio_name_pair[gpio_channel] = name
            self._register_gpio(self.gpio_name_pair)

    def __delitem__(self, gpio_channel):
        if isinstance(gpio_channel, int) and self.gpio_name_pair.get(gpio_channel):
            self.gpio_name_pair[gpio_channel] = ""
            self._register_gpio(self.gpio_name_pair)
            self.cleanup(gpio_channel)

    def __getitem__(self, gpio_channel):
        return self.gpio_name_pair.get(gpio_channel)

    def cleanup(self, channel=None):
        """ Clean all GPIO channels used in program instance
        if channel not specified. Otherwise, clean provided
        GPIO channel. """
        if not channel:
            for gpio_channel in self.registered_gpio:
                GPIO.cleanup(gpio_channel)

    def setup(self):
        """ Setup function to register GPIO input channels. """
        self._setup_gpio_in()

    def start_callback(self):
        """ Start GPIO callbacks. Add event detect to registered
        channels and assign channels to designated callback functions. """
        self._add_event_detect()
        self._add_event_callback()

    def read_input(self):
        for gpio_channel in self.registered_gpio:
            self.print_message(gpio_channel)
            time.sleep(1)

    def _setup_gpio_in(self):
        """ Set up GPIO IN for channels registered in the class
        instance. """
        for gpio_channel in self.registered_gpio:
            GPIO.setup(gpio_channel, GPIO.IN)

    def _add_event_detect(self):
        """ Called after self._setup_gpio_in. Add event detect for
        channels registered in the class instance. """
        for gpio_channel in self.registered_gpio:
            GPIO.add_event_detect(gpio_channel, GPIO.BOTH, bouncetime=300)

    def _add_event_callback(self):
        """ Called after self._add_event_detect. Apply event callback for
        channels registered in the class instance. Each callback is unique
        to the GPIO channel. """
        for gpio_channel in self.registered_gpio:
            GPIO.add_event_callback(gpio_channel, self.callback[gpio_channel])

    def _register_gpio(self, gpio_map):
        """ Set instance variable self.registered_gpio, a dictionary of 
        occupied GPIO channels with (e.g. plant) name. """
        for gpio_channel, name in gpio_map.items():
            if gpio_channel not in self.gpio_name_pair:
                raise KeyError(
                    f"{gpio_channel} is not a valid GPIO channel in Raspberry Pi model {self.pi_model}."
                )
            if len(name) > 16:
                raise ValueError(f'"{name}" has {len(name)} chars. Maximum char is 16.')
            self.gpio_name_pair[gpio_channel] = gpio_map[gpio_channel]

        self.registered_gpio = [
            gpio for gpio, name in self.gpio_name_pair.items() if name
        ]
