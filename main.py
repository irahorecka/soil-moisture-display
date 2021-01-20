from soil import Soil, led, lcd
import datetime
import time

# gpio channel: plant name
plant_map = {
    19: "Prls/Jade Pothos",
    20: "Calathea Mdln",
    21: "Micans Pothos",
}
my_plants = Soil(plant_map)
# an example of adding a gpio channel with a plant name
my_plants[26] = "Golden Pothos"
# set callback=True to detect real-time changes in moisture
my_plants.setup(callback=False, display="lcd")

if __name__ == "__main__":
    try:
        # display welcome message for 5 seconds
        lcd.display("Let's detect", "soil moisture!", duration=5)
        while True:
            led.on(channel=4)
            my_plants.readout_moisture(duration=3)
            led.off(channel=4)

            # display current time and date during 2 min interim
            datetime_interim = datetime.datetime.now() + datetime.timedelta(0, 120)
            while datetime.datetime.now() < datetime_interim:
                lcd.display_datetime("US/Pacific")
                # add slight latency - we don't need to display datetime every chance we can get
                time.sleep(0.1)

    except KeyboardInterrupt:
        my_plants.cleanup()
