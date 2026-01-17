from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

plt.style.use('ggplot')
fig, ax = plt.subplots()

path = Path('weather_data/sitka_weather.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

ax.plot(dates, highs, color="red")

ax.set_title("Daily High Tempratures, July 2021 (Sitka, Alaska)", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temprature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
