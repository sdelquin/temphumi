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

On the PC:

```bash
$ cp config.tmpl.py config.py
# set your own values
$ pip install -r requirements.txt
$ make deploy
$ make
```

On the NodeMCU:

```python
>>> import temphumi
>>> temphumi.run()
```

## Tracking

Data is logged into [dweet.io](http://dweet.io/):

![dweet](img/dweet.png) 

Depending on your "thing" name, you get different url, but, just to show the behaviour, you can check my data: http://dweet.io/follow/sdelquin
