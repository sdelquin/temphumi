import config
import requests
import dateparser
import csv
import os.path


def get_data():
    url = f"https://dweet.io/get/dweets/for/{config.DWEET_THING}"
    r = requests.get(url)
    dweets = r.json()
    temperature = dweets["with"][0]["content"]["temperature"]
    humidity = dweets["with"][0]["content"]["humidity"]
    timestamp = dateparser.parse(
        dweets["with"][0]["created"],
        settings={"TO_TIMEZONE": config.TIME_ZONE}
    ).strftime("%y-%m-%d %H:%M")
    return timestamp, temperature, humidity


def save_data(data):
    if os.path.isfile(config.CSV_FILE):
        with open(config.CSV_FILE, "a") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(data)
    else:
        with open(config.CSV_FILE, "w") as csv_file:
            csv_file.write("{}\n".format(",".join(config.FIELD_NAMES)))


data = get_data()
save_data(data)
