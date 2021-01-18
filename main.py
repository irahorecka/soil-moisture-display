from soil import Soil


def main():
    # gpio channel: plant name
    plant_map = {
        16: "Golden pothos",
        19: "Prls/Jade pothos",
        20: "Dinosaur plant",
        21: "Money plant",
    }
    my_plants = Soil(plant_map)
    # an example of adding a gpio channel with a plant name
    my_plants[26] = "Velvet plant"
    my_plants.setup()
    return my_plants


if __name__ == "__main__":
    try:
        while True:
            plant_session = main()
    except KeyboardInterrupt:
        plant_session.cleanup()
