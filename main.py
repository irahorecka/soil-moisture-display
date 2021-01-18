from soil import Soil
import time

# gpio channel: plant name
plant_map = {
    16: "Golden Pothos",
    19: "Prls/Jade Pothos",
    20: "Calathea Mdln",
    21: "Chns Money Plant",
}
my_plants = Soil(plant_map)
# an example of adding a gpio channel with a plant name
my_plants[26] = "Micans Pothos"
my_plants.setup()

# if you want to add callback, i.e. detect change in moisture, call...
# my_plants.start_callback()

if __name__ == "__main__":
    try:
        while True:
            my_plants.read_input()
            # wait 9 seconds before re-reading input
            time.sleep(9)
    except KeyboardInterrupt:
        my_plants.cleanup()
