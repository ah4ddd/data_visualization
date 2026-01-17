from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

plt.style.use('ggplot')
fig, ax = plt.subplots()

path = Path('weather_data/death_valley_weather.csv')
path_2 = Path('weather_data/sitka_weather.csv')
lines = path.read_text().splitlines()
lines_2 = path_2.read_text().splitlines()

reader = csv.reader(lines)
reader_2 = csv.reader(lines_2)

header_row = next(reader)
header_row_2 = next(reader_2)

datex, highx, lowx = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        datex.append(current_date)
        highx.append(high)
        lowx.append(low)

ax.plot(datex, highx, color="green", alpha=1)
ax.plot(datex, lowx, color="yellow", alpha=1)
ax.fill_between(datex, highx, lowx, facecolor='yellow', alpha=0.1)

dates, highs, lows = [], [], []
for row in reader_2:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

ax.set_title("Daily High and Low Tempratures comparison between Death Valley, California and Sitka Alaska", fontsize=20)
ax.set_xlabel("Green-Yellow = Death Valley, Red-Blue = Sitka Alaska", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temprature (F)", fontsize=16)
ax.tick_params(labelsize=16)

ax.plot(dates, highs, color="red", alpha=1)
ax.plot(dates, lows, color="blue", alpha=1)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

plt.show()
