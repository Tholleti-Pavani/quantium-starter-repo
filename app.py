import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("data/formatted_output.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50"
            }),

    # Radio buttons
    dcc.RadioItems(
        id="region-selector",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        labelStyle={"display": "inline-block", "margin": "10px"},
        style={"textAlign": "center"}
    ),

    dcc.Graph(id="sales-graph")

],
    style={
        "backgroundColor": "#f4f6f7",
        "padding": "30px"
    })


# Callback to update graph
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-selector", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Group by date
    filtered_df = filtered_df.groupby("date")["sales"].sum().reset_index()

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Sales Over Time",
        labels={"date": "Date", "sales": "Total Sales"}
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)