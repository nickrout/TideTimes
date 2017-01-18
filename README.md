# TideTimes

*This code is not yet finished!!!*

Python script to get tide times for any location supported by tidespy.com and report the last tide and next two tides.

This is based on ideas from @imikerussell at https://github.com/imikerussell/TideTimes - I forked his code but largely used it for inspiration. Using a data source that gives a json response, rather than scraping a website, makes it considerably easier.

So most of the code is mine, and that means it is pretty inefficient, but I'll tweak it over time. IT IS NOT YET READY. 

Install dependancies:

```pip install requests```

```pip install bs4```
    
To configure:

```cp configspy.py.example configspy.py```

```nano config.py```

Edit the *api_key*, *location* and *basedir* variables. *api_key*  is available for free from [TideSpy](http://tidespy.com/client/RawApi.php). *location* should be the 4 digit number obtainable from TideSpy. *basedir* should be set to the directory your tidesspy.py and tideupdatespy.py are store. Your data will also be stored there. *Please note that this is different to @imikerussell 's config naming.




To get started:

Set up a cronjob `crontab -e` at 06:00, or some other tme suitable to you:

```0 6 * * * /usr/bin/python /home/hass/TideTimes/tides.py```

Test it! Run `python tideupdate.py` and check for an output like this:

```
Tide Times Location: Sandown (Beach)
Next High Tide: 22:34
Next High Tide Height: 4.1
Next Low Tide: 04:11
Next Low Tide Height: 0.8
```

## Intergration with Home Assistant

Home Assistant is an amazing, open source, home automation platform. If you're into home automation and own a few devices you should think about linking them together inside [Home Assistant](https://home-assistant.io/)!

Here's how TideTimes looks inside Home Assistant:

<img src="https://raw.githubusercontent.com/imikerussell/TideTimes/master/tidetimes.png" width="441" alt="TideTimes works with Home Assistant">

Example sensor setup (using the [Command Line sensor](https://home-assistant.io/components/sensor.command_line/) from Home Assistant):

```
- platform: command_line
  name: Tide Times Location
  command: "python /home/hass/TideTimes/tideupdate.py | grep 'Tide Times Location:' | sed 's/^.*: //'"

- platform: command_line
  name: High Tide Time
  command: "python /home/hass/TideTimes/tideupdate.py | grep 'Next High Tide:' | sed 's/^.*: //'"

- platform: command_line
  name: High Tide Height
  command: "python /home/hass/TideTimes/tideupdate.py | grep 'Next High Tide Height:' | sed 's/^.*: //'"
  unit_of_measurement: "m"

- platform: command_line
  name: Low Tide Time
  command: "python /home/hass/TideTimes/tideupdate.py | grep 'Next Low Tide:' | sed 's/^.*: //'"

- platform: command_line
  name: Low Tide Height
  command: "python /home/hass/TideTimes/tideupdate.py | grep 'Next Low Tide Height:' | sed 's/^.*: //'"
  unit_of_measurement: "m"
```

Example group (to get the sensors in a box of their own):

```
Tide Times:
  - sensor.tide_times_loaction
  - sensor.high_tide_time
  - sensor.high_tide_height
  - sensor.low_tide_time
  - sensor.low_tide_height
```

Example customize (for cool icons):

```
sensor.tide_times_loaction:
  icon: mdi:fish

sensor.high_tide_time:
  icon: mdi:flag-variant

sensor.high_tide_height:
  icon: mdi:elevation-rise

sensor.low_tide_time:
  icon: mdi:flag-outline-variant

sensor.low_tide_height:
  icon: mdi:elevation-decline
```
