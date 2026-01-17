from pathlib import Path
import csv

path = Path('weather_data/sitka_weather.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)
