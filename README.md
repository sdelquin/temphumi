# TempHumi

Sensor of *temperature* and *humidity* using `micropython`.

## Ingredients

### NodeMCU (ESP8266)

![NodeMCU](img/NodeMcu.jpg)

### DHT22

![DHT22](img/DHT22.png)

### Protoboard

![Protoboard](img/protoboard.jpg)

### Cables

- Cables to connect components (blue, red, and black).
- MicroUSB to USB cable to connect NodeMCU with PC.

## Scheme

![Fritzing](img/DHT_scheme.png) 

## Picture

![Real](img/DHT_real.jpg) 

## Usage

> **IMPORTANT**: Use a **DATA** cable (*usb-microusb*) to connect the ESP8266 with the computer. Otherwise it won't be recognised and no device will bring up.

Set the corresponding settings in `.env` file:

~~~console
$ vi .env
# ...
~~~

Install requirements:

~~~console
$ pipenv install
~~~

Deploy files to ESP8266:

~~~console
$ python manage.py deploy
~~~

**Reset the NodeMCU and have fun!** (press the `RST` button on board)

> When resseting the ESP8266 it will try to run `main.py`

## Tracking

Data is logged into [dweet.io](http://dweet.io/):

![dweet](img/dweet.png) 

Depending on your "thing" name, you get different url, but, just to show the behaviour, you can check my data: http://dweet.io/follow/sdelquin
