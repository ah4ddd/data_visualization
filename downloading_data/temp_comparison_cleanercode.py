from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

def read_weather_data(path, date_idx, high_idx, low_idx):
    dates, highs, lows = [], [], []

    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    for row in reader:
        try:
            current_date = datetime.strptime(row[date_idx], '%Y-%m-%d')
            high = int(row[high_idx])
            low = int(row[low_idx])
        except ValueError:
            continue
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    return dates, highs, lows

plt.style.use('ggplot')
fig, ax = plt.subplots()

dv_path = Path('weather_data/death_valley_weather.csv')
sitka_path = Path('weather_data/sitka_weather.csv')

dv_dates, dv_highs, dv_lows = read_weather_data(dv_path, 2, 3, 4)
sitka_dates, sitka_highs, sitka_lows = read_weather_data(sitka_path, 2, 4, 5)

ax.plot(dv_dates, dv_highs, color="green", label="Death Valley High")
ax.plot(dv_dates, dv_lows, color="yellow", label="Death Valley Low")
ax.fill_between(dv_dates, dv_highs, dv_lows, facecolor='yellow', alpha=0.1)

ax.set_title("Daily Highs and Lows Tempratures comparison", fontsize=20)
ax.set_ylabel("Temprature (F)", fontsize=16)

ax.plot(sitka_dates, sitka_highs, color="red", label="Sitka High")
ax.plot(sitka_dates, sitka_lows, color="blue", label="Sitka Low")
ax.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.1)

ax.legend()
plt.show()
