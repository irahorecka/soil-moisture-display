from .rpimodel import RPi_3BP


class Soil(RPi_3BP):
    """ Simple API to hook up and detect soil moisture hardware to your
    Raspberry Pi. """

    def __init__(self, gpio_map):
        super().__init__()
        if not isinstance(gpio_map, dict):
            raise TypeError("Expected <dict> argument.")
        self._register_gpio(gpio_map)

    def __setitem__(self, gpio_channel, name):
        if isinstance(gpio_channel, int) and gpio_channel in self.callback_method:
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
            for channel in self.registered_gpio:
                self.gpio_cleanup(channel)
        else:
            if not isinstance(channel, int):
                raise ValueError("GPIO channel must be of type <int>.")
            self.cleanup(channel)

    def setup(self, callback=False, display="lcd"):
        """ Setup function to register GPIO input channels with option
        to add event callbacks. """
        self.display_medium = display
        self._setup_gpio_in()
        if callback:
            self._add_event_detect()
            self._add_event_callback()

    def readout_moisture(self, **kwargs):
        """ Read moisture in real-time from registered GPIO input channels
        and display on selected medium. """
        for gpio_channel in self.registered_gpio:
            self.display_moisture(
                gpio_channel, **kwargs,
            )

    def _setup_gpio_in(self):
        """ Set up GPIO.IN (mode="in") for channels registered in the class
        instance. """
        for gpio_channel in self.registered_gpio:
            self.gpio_setup(gpio_channel, mode="in")

    def _add_event_detect(self):
        """ Called after self._setup_gpio_in. Add event detect for
        channels registered in the class instance. """
        for gpio_channel in self.registered_gpio:
            self.gpio_add_event_detect(gpio_channel, bouncetime=300)

    def _add_event_callback(self):
        """ Called after self._add_event_detect. Apply event callback for
        channels registered in the class instance. Each callback is unique
        to the GPIO channel. """
        for gpio_channel in self.registered_gpio:
            self.gpio_add_event_callback(gpio_channel)

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
