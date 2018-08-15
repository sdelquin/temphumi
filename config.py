from prettyconf import config

FILES_TO_DEPLOY = ('main.py', 'uconfig.py')
CSV_FILE = 'sensor.csv'
FIELD_NAMES = ('timestamp', 'temperature', 'humidity')
TTY_HANDLER = config('TTY_HANDLER', default='ttyUSB0')
WIFI_SSID = config('WIFI_SSID', default='put here your wifi ssid')
WIFI_PASSWORD = config('WIFI_PASSWORD', default='put here your wifi passwd')
DWEET_THING = config('DWEET_THING', default='name of your dweet thing')
TIME_ZONE = config('TIME_ZONE', default='UTC')
