from pathlib import Path
import csv

path = Path('weather_data/sitka_weather.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
