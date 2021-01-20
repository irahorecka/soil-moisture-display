from soil import Soil, lcd
import time

# gpio channel: plant name
plant_map = {
    16: "Peace Lily",
    19: "Prls/Jade Pothos",
    20: "Calathea Mdln",
    21: "Micans Pothos",
    26: "Golden Pothos",
}
my_plants = Soil(plant_map)
my_plants.setup(callback=True, display="lcd")

if __name__ == "__main__":
    try:
        # let's display a welcome message for 5 seconds
        lcd.display("Let's detect", "soil moisture!", duration=5)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # clean up GPIO channels on application exit
        my_plants.cleanup()
