import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Read your processed file
df = pd.read_csv("data/formatted_output.csv")

# Convert Date column to proper date format
df["date"] = pd.to_datetime(df["date"])

# Sort by Date
df = df.sort_values("date")

# Group by Date and sum sales
df = df.groupby("date")["Sales"].sum().reset_index()

# Create line chart
fig = px.line(df, x="date", y="Sales")

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Analysis"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)