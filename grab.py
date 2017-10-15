import config
import requests
import dateparser
import sqlite3

url = f"https://dweet.io/get/dweets/for/{config.DWEET_THING}"
r = requests.get(url)
dweets = r.json()
temperature = dweets["with"][0]["content"]["temperature"]
humidity = dweets["with"][0]["content"]["humidity"]
timestamp = dateparser.parse(
    dweets["with"][0]["created"],
    settings={"TO_TIMEZONE": config.TIME_ZONE}
).strftime("%y-%m-%d %H:%M:%S")

db_connection = sqlite3.connect(config.DATABASE)
with db_connection:
    db_cursor = db_connection.cursor()
    sql = f"INSERT INTO data (timestamp, temperature, humidity) VALUES \
        ('{timestamp}', {temperature}, {humidity})"
    db_cursor.execute(sql)
