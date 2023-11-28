import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc

# Load the dataset
data = pd.read_excel("C:/Users/Chandru/OneDrive/Desktop/Python Visuals/Sample - Superstore.xls", sheet_name="Orders")

# Create a Dash application
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the app layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='subcategory-dropdown',
                options=[{'label': subcat, 'value': subcat} for subcat in data['Sub-Category'].unique()],
                value=data['Sub-Category'].unique(),
                multi=True
            )
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='3d-scatter-chart')
        ])
    ])
])

# Define callback to update graph
@app.callback(
    Output('3d-scatter-chart', 'figure'),
    [Input('subcategory-dropdown', 'value')]
)
def update_graph(selected_subcategories):
    filtered_data = data[data['Sub-Category'].isin(selected_subcategories)]
    fig = px.scatter_3d(filtered_data, x='Sales', y='Profit', z='Quantity', color='Sub-Category', title='3D Scatter Plot - Sales, Profit, and Quantity by Sub-Category')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8059)
