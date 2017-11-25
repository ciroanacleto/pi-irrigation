#!/usr/bin/python3

import time
import schedule
import RPi.GPIO as GPIO
import logging

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(format= LOG_FORMAT,
                    filename='./pi_irrigation.log',
                    level=logging.INFO)
log = logging.getLogger()

relay_pin = 12
first_hour = "10:00"
second_hour = "22:00"
watering_time = 360 #6 min

def setup():
    log.info('Config pins')
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.output(relay_pin, GPIO.HIGH)

def irrigate():
    GPIO.output(relay_pin, GPIO.LOW)
    log.info('Solenoid is on')

    time.sleep(watering_time)

    GPIO.output(relay_pin, GPIO.HIGH)
    log.info('Solenoid is off')

def destroy():
    GPIO.output(relay_pin, GPIO.HIGH)
    log.info('Cleanning up pins')
    GPIO.cleanup()

if __name__ == '__main__':
    setup()

    log.info('Setting first irrigation time to ' + first_hour)
    schedule.every().day.at(first_hour).do(irrigate)

    log.info('Setting second irrigation time to ' + second_hour)
    schedule.every().day.at(second_hour).do(irrigate)
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        destroy()
    finally:
        destroy()
