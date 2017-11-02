# pi-irrigation
A Raspberry pi automatic irrigation project

This project works scheduling 2 periods for irrigation using the [schedule library](https://github.com/dbader/schedule). 

The program must be added to crontab to run at every raspberry pi reboot. To do this run the command:

```
crontab -e
```

Type:

``@reboot sudo python /home/pi/pi-irrigation/pi_irrigation.py``

Open pi_irrigation.py file and choose which Raspberry pi GPIO pin your relay board is pluged on _relay_pin_ variable. The program is configured to use the GPIO physical location.

Type what hour you desire to activate the solenoid on _first_hour_ and _second_hour_ variables. It was choosen watering 2 times at day.

And finally for how many seconds the solenoid must stay open on _watering_time_ variable.

On the folder _/project_images_ there is a project schema made in [fritzing app](http://fritzing.org).