from die import Die
import plotly.express as px

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

fig = px.bar(x=poss_results,
             y=frequencies,
             title="Results of Rolling One D6 1,000 Times",
             labels={"x":"Results", "y":"Frequency of Results"}
             )
fig.show()
