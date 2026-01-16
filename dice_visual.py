from matplotlib.axis import XAxis
from die import Die
import plotly.express as px

die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_results = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_results+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

fig = px.bar(x=poss_results,
             y=frequencies,
             title="Results of Rolling Two D6 1,000 Times",
             labels={"x":"Results", "y":"Frequency of Results"}
             )
fig.update_layout(xaxis_dtick=1)
fig.show()
