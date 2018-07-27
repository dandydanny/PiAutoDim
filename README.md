# PiAutoDim
![image](https://github.com/dandydanny/PiAutoDim/blob/master/screenshot.gif)
Auto-Dimming for the Raspberry-Pi 7" Touchscreen LCD Display

### What?
Code and schematic diagram to automatically dim the backlight of the Raspberry-Pi Official 7" Touchscreen LCD display. Based on [this light-sensor example](https://gpiozero.readthedocs.io/en/stable/recipes.html#light-sensor) from [GPIO Zero](https://gpiozero.readthedocs.io/en/stable/).

### Why?
1. I don't want to be blinded by the bright LCD backlight at night
1. Provide dynamic display brightness adjustment for optimal display contrast in all lighting conditions

### Where?
On my nightstand, but you can see how it works at this [demo link](https://twitter.com/dandydanny/status/1020504279797379072)

### Changelog
* v0.1 - Initial release

### Hardware Setup


### Software Setup
Edit the backlight permissions file:

`sudo nano /etc/udev/rules.d/backlight-permissions.rules`

...to allow read and write permissions to all users:

`SUBSYSTEM=="backlight",RUN+="/bin/chmod 666 /sys/class/backlight/%k/brightness /sys/class/backlight/%k/bl_power"`

### About
Daniel is a web developer seeking opportunities, beverage socials, and late-night taco runs. [dandydanny.github.io](https://git.io/vxurG)
