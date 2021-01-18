from soil import Soil

# gpio channel: plant name
plant_map = {
    16: "Nanna's pathos",
    19: "Variegated pathos",
    20: "Yale House plant",
    21: "Money plant",
}
my_plants = Soil(plant_map)
# an example of adding a gpio channel with a plant name
my_plants[26] = "Velvet plant"
my_plants.setup()

try:
    while True:
        pass
except KeyboardInterrupt:
    my_plants.cleanup()
