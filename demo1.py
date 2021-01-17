from soil import Soil
import time

plant_map = {
    20: "Coffee plant",
    21: "Palm tree",
}
my_plants = Soil(plant_map)
my_plants.setup()

while True:
    time.sleep(1)
