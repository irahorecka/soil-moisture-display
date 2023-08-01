soil-moisture-display
======================

A Raspberry Pi project to detect and display my plants' soil moisture (`image <https://i.imgur.com/oF2Dy9f.jpg>`__). My project is configured for the Raspberry Pi 3B+ using Python 3.7.3.

Running the application
-----------------------
It's as simple as cloning this repository and running:

.. code::

    pip3 install -r requirements.txt

    python3 main.py

API
---
This project is designed to provide a fairly simple API out of the box.

For example, let's set up this instance:
    1. We want to set up 5 soil moisture sensors
    2. We want these sensors to have callback (i.e. notify in real-time when soil moisture changes)
    3. We want to display this information on a 16x2 I2C LCD display.


.. code:: python

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

Hardware
--------
The bare minimum hardware to run the example above are:
    1. `Raspberry Pi 3B+ <https://www.adafruit.com/product/3775?gclid=CjwKCAiAxp-ABhALEiwAXm6IyX-H5MpH2sCIu2blt1z280QzN5u27OJqmXk_ahaWeyCdg-iEFa8j3BoCj8gQAvD_BwE>`__
    2. `Soil Moisture Sensor <https://www.amazon.com/KeeYees-Sensitivity-Moisture-Watering-Manager/dp/B07QXZC8TQ/ref=asc_df_B07QXZC8TQ/?tag=hyprod-20&linkCode=df0&hvadid=343238573411&hvpos=&hvnetw=g&hvrand=8836444678364226758&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9031923&hvtargid=pla-757549749596&psc=1&tag=&ref=&adgrpid=71762478951&hvpone=&hvptwo=&hvadid=343238573411&hvpos=&hvnetw=g&hvrand=8836444678364226758&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9031923&hvtargid=pla-757549749596>`__
    3. `16x2 I2C LCD Display <https://www.amazon.com/GeeekPi-Character-Backlight-Raspberry-Electrical/dp/B07S7PJYM6>`__
    4. `Jumper Wires <https://www.amazon.com/EDGELEC-Breadboard-Optional-Assorted-Multicolored/dp/B07GD2BWPY/ref=pd_bxgy_img_3/138-1998102-2136103?_encoding=UTF8&pd_rd_i=B07GD2BWPY&pd_rd_r=6ef1b01c-f0b3-41c0-9c3b-823a9ae973ec&pd_rd_w=LuogT&pd_rd_wg=IRWFy&pf_rd_p=f325d01c-4658-4593-be83-3e12ca663f0e&pf_rd_r=3Z5VTS5DNDF558PZ11KK&psc=1&refRID=3Z5VTS5DNDF558PZ11KK>`__
    5. `Bread Board <https://www.amazon.com/Breadboards-Solderless-Breadboard-Distribution-Connecting/dp/B07DL13RZH/ref=pd_bxgy_img_2/138-1998102-2136103?_encoding=UTF8&pd_rd_i=B07DL13RZH&pd_rd_r=7fc8bec8-868c-4966-a9bd-83c4ab8054ef&pd_rd_w=kGG9s&pd_rd_wg=Bs9Cl&pf_rd_p=f325d01c-4658-4593-be83-3e12ca663f0e&pf_rd_r=PXM8J6SEHKTEWA7HXFV3&psc=1&refRID=PXM8J6SEHKTEWA7HXFV3>`__

Useful Resources
----------------
Listed are resources I found useful in setting up hardware:
    1. `Wiring 16x2 I2C LCD Display <https://i.imgur.com/kSKlNOX.png>`__
    2. `Setting up soil moisture sensors w/ RPi <https://www.instructables.com/Soil-Moisture-Sensor-Raspberry-Pi/>`__
            
Contribute
----------
- `Issues Tracker <https://github.com/irahorecka/SoilMoistureDisplay/issues>`__

Support
-------
If you are having issues or would like to propose a new feature, please use the `issues tracker <https://github.com/irahorecka/SoilMoistureDisplay/issues>`__.

License
-------
This project is licensed under the MIT license.
