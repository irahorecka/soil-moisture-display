from soil import Soil, led, lcd
import time

# gpio channel: plant name
plant_map = {
    16: "Golden Pothos",
    19: "Prls/Jade Pothos",
    20: "Calathea Mdln",
    21: "Micans Pothos",
}
my_plants = Soil(plant_map)
# an example of adding a gpio channel with a plant name
my_plants[26] = "Chns Money Plant"
# set callback=True to detect real-time changes in moisture
my_plants.setup(callback=False, display="lcd")

if __name__ == "__main__":
    try:
        lcd.display("Let's detect", "soil moisture!")
        while True:
            led.on(channel=4)
            my_plants.readout_moisture()
            led.off(channel=4)
            # wait 59 seconds before re-reading input (~ 1 min)
            # display current time and date during interim
            for _ in range(59):
                lcd.display_datetime()
                time.sleep(1)
    except KeyboardInterrupt:
        my_plants.cleanup()
