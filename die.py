import plotly.express as px
import pandas

x = [1,2,3,4]
y = [10,20,15,30]

fig = px.line(
    x=x,
    y=y,
    title="My First Plotly Chart",
    labels={"x": "X Axis", "y": "Y Axis"},
    markers=True
)
fig.show()
