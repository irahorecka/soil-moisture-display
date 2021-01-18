
#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# GPIO SETUP
channel_20 = 20
channel_21 = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel_20, GPIO.IN)
GPIO.setup(channel_21, GPIO.IN)


# def callback_20(channel):
#     if GPIO.input(channel):
#         print("Coffee plant is fine.")
#     else:
#         print("Coffee plant is fine.")


# def callback_21(channel):
#     if GPIO.input(channel):
#         print("Pathos plant is fine.")
#     else:
#         print("Pathos plant is fine.")


# GPIO.add_event_detect(
#     channel_20, GPIO.BOTH, bouncetime=100
# )  # let us know when the pin goes HIGH or LOW
# GPIO.add_event_detect(channel_21, GPIO.BOTH, bouncetime=100)
# GPIO.add_event_callback(
#     channel_20, callback_20
# )  # assign function to GPIO PIN, Run function on change
# GPIO.add_event_callback(channel_21, callback_21)

# infinite loop
if __name__ == "__main__":
    while True:
        if GPIO.input(channel_20) == True:
            print('true')
        else:
            print('false')
        time.sleep(1)