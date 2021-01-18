from soil import Soil, led
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
my_plants.setup()

# if you want to add callback, i.e. detect change in moisture, call...
# my_plants.start_callback()

if __name__ == "__main__":
    try:
        while True:
            led.on(channel=4)
            my_plants.read_input()
            led.off(channel=4)
            # wait 9 seconds before re-reading input
            time.sleep(9)
    except KeyboardInterrupt:
        my_plants.cleanup()
