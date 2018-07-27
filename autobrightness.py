# PiAutoDim
# Auto-Dimming for the Raspberry-Pi 7" Touchscreen LCD Display
# Based on https://gpiozero.readthedocs.io/en/stable/recipes.html#light-sensor

from gpiozero import LightSensor
from time import sleep

# Desired maximum & minimum backlight values
max = 255
min = 12
prev = 0
offset = 10
delta = 0

# Open backlight control 'file' for writing
f = open('/sys/class/backlight/rpi_backlight/brightness', 'w')

# Instantiate sensor object, set charge time suitable for 10uF capacitor
sensor = LightSensor(18, charge_time_limit=0.2, threshold=0.1)

while True:
    # Get light sensor value, map to 0-255
    lightValue = round(255 * sensor.value + offset)

    # Keep values within defined maximum-minimum values
    if lightValue > 240:
        lightValue = max
    if lightValue < min:
        lightValue = min
    
    # Calculate change in brightness value
    delta = abs(lightValue - prev)

    # Only write (change) backlight value if there's sensor level change
    if delta > 5:
        prev = lightValue
        f.seek(0)
        f.write(str(lightValue))
        f.truncate()
sleep(1)