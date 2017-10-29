#!/usr/bin/python3.4

import time
import schedule
import RPi.GPIO as GPIO

relay_pin = 12
first_hour = "10:00"
second_hour = "22:00"
watering_time = 600 #10 min

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.output(relay_pin, GPIO.HIGH)

def irrigate():
    GPIO.output(relay_pin, GPIO.LOW)
    print("Solenoid is on")

    time.sleep(watering_time)

    GPIO.output(relay_pin, GPIO.HIGH)
    print("Solenoid is off")

def destroy():
    GPIO.output(relay_pin, GPIO.HIGH)
    print("Destroying")
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    schedule.every().day.at(first_hour).do(irrigate)
    schedule.every().day.at(second_hour).do(irrigate)
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        destroy()
    finally:
        destroy()
