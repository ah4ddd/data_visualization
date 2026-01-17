from pathlib import Path
import csv
import matplotlib.pyplot as plt

plt.style.use('ggplot')
fig, ax = plt.subplots()

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

ax.plot(highs, color="red")

ax.set_title("Daily High Tempratures, July 2021 (Sitka, Alaska)", fontsize=24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temprature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
