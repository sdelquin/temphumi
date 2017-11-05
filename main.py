from machine import Pin
from dht import DHT22
import time
import network
import urequests
import config

PIN_LABEL = {
    "D5": 14,
}


def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(config.WIFI["ssid"], config.WIFI["password"])
    return sta_if.isconnected()


def send_data(temperature, humidity):
    url = "https://dweet.io/dweet/for/{}?temperature={}&humidity={}".format(
        config.DWEET_THING,
        temperature,
        humidity
    )
    r = urequests.get(url)
    r.close()


def run():
    connect_to_wifi()
    d = DHT22(Pin(PIN_LABEL["D5"]))
    while True:
        d.measure()
        send_data(d.temperature(), d.humidity())
        time.sleep(1)


if __name__ == "__main__":
    run()
