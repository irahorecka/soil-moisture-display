from soil import Soil
import time

# gpio pin: plant name
plant_map = {
    16: "Nanna's pathos",
    19: "Variegated pathos",
    20: "Yale House plant",
    21: "Money plant",
    26: "Velvet plant",
}
my_plants = Soil(plant_map)
my_plants.setup()

while True:
    time.sleep(1)
