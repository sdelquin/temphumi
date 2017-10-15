from machine import Pin
from dht import DHT22
import time

PIN_LABEL = {
    "D5": 14,
}


def run():
    d = DHT22(Pin(PIN_LABEL["D5"]))
    while True:
        d.measure()
        print(d.temperature(), d.humidity())
        time.sleep(1)
