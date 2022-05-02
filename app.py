from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

dash_app = Dash(__name__)

df = pd.read_csv("./data/processed_sales_data.csv")
df = df.sort_values(by="date")

dash_app.layout = html.Div(children=[
    html.H1(id="header",
        children='Sales Visualiser'),

    dcc.Graph(
        id='sales-graph'
    ),

    html.Div([
        html.Label('Regions'),
        dcc.RadioItems(
            ['north', 'east','south', 'west', 'all'], 'north' ,id='selected-region',)
    ], className="flex-container"),


])

@dash_app.callback(
    Output('sales-graph', 'figure'),
    Input('selected-region', 'value'),
    )


def update_graph(selected_region):
    
    if selected_region in ['north', 'east','south', 'west']:
        new_df = df[df['region'] == selected_region]
        fig = px.line(new_df, x="date", y="sales", color='region')
    else:
        fig = px.line(df, x="date", y="sales", color='region')
 
    return fig

if __name__ == '__main__':
    dash_app.run_server(debug=True)
