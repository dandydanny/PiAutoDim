# PiAutoDim
![image](https://github.com/dandydanny/PiAutoDim/blob/master/screenshot.gif)
Auto-Dimming for the Raspberry-Pi 7" Touchscreen LCD Display

### What?
Code and schematic diagram to automatically dim the backlight of the Raspberry-Pi Official 7" Touchscreen LCD display. Based on [this light-sensor example](https://gpiozero.readthedocs.io/en/stable/recipes.html#light-sensor) from [GPIO Zero](https://www.raspberrypi.org/blog/gpio-zero-a-friendly-python-api-for-physical-computing/).

### Why?
1. I don't want to be blinded by the bright LCD backlight at night
1. Provide dynamic display brightness adjustment for optimal display contrast in all lighting conditions

### Where?
On my nightstand, but you can see how it works at this [demo link](https://twitter.com/dandydanny/status/1020504279797379072)

### Changelog
* v0.1 - Initial release

### Hardware Setup
Parts needed:
* [Cds photo cell / photoresistor](https://www.adafruit.com/product/161) ([photo transistor](https://www.adafruit.com/product/2831) OK)
* 10µF 16V capacitor (if using 1µF, edit `charge_time_limit` argument in `autobrightness.py` so that the `charge_time_limit=0.01`)
* [Female jumper wires](https://www.adafruit.com/product/1951)

Connection diagram:
![image](https://github.com/dandydanny/PiAutoDim/blob/master/connection.png)

### Software Setup
#### Edit the backlight permissions file to allow read and write permissions to all users:

`sudo nano /etc/udev/rules.d/backlight-permissions.rules`

Insert:

`SUBSYSTEM=="backlight",RUN+="/bin/chmod 666 /sys/class/backlight/%k/brightness /sys/class/backlight/%k/bl_power"`

#### Enable autorun of `autobrightness.py` on boot, by making it a `systemd` service


In `/etc/systemd/system/`, make a `autobrightness.service` file.

`touch autobrightness.service`

Open this file in an editor:

`sudo nano autobrightness.service`

Put in following:
```
[Unit]
Description=Get auto brightness service running at boot
After=mosquitto.service mysql.service

[Service]
ExecStart=/usr/bin/python3 /home/pi/autobrightness/autobrightness.py
Restart=always
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=autobrightness
User=pi
Group=pi

[Install]
WantedBy=multi-user.target
```

Press `CTRL-O` to save, and `CTRL-X` to exit nano editor.

Enable service to run on startup:

`sudo systemctl enable autobrightness.service`

Start autobrightness service (for current boot):

`sudo systemctl start autobrightness.service`

Check if it's running:

`systemctl status autobrightness.service`

Adjust the amount of light falling on the Cds sensor. The backlight level should change accordingly.

### About
Daniel is a web developer seeking opportunities, beverage socials, and late-night taco runs. [dandydanny.github.io](https://git.io/vxurG)
