from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from data import df


all_regions = df['region'].unique()


layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
            html.H3("Динамика потребления разных алкогольных напитков"),
            html.P("Графики с динамикой потребления различных алкогольных напитков по областям для наглядного сравнения и анализа данных."),
            html.Hr(style={'color': 'black'}),
        ], style={'textAlign': 'center'}))
    ]),
    dbc.Row([
        dbc.Col([
            html.P("Регион:"),
            dcc.Dropdown(
                id='region-dropdown',
                options=[{'label': region, 'value': region} for region in all_regions],
                value=all_regions[0]
            )
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='beer-graph'), width=6),
        dbc.Col(dcc.Graph(id='wine-graph'), width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='brandy-graph'), width=4),
        dbc.Col(dcc.Graph(id='vodka-graph'), width=4),
        dbc.Col(dcc.Graph(id='champagne-graph'), width=4)
    ])
])

@callback(
    [Output('beer-graph', 'figure'),
     Output('wine-graph', 'figure'),
     Output('brandy-graph', 'figure'),
     Output('vodka-graph', 'figure'),
     Output('champagne-graph', 'figure')],
    [Input('region-dropdown', 'value')]
)
def update_graphs(selected_region):
    filtered_df = df[df['region'] == selected_region]

    beer_fig = px.line(filtered_df, x='year', y='beer', title='Потребление пива')
    beer_fig.update_layout(height=350)

    wine_fig = px.line(filtered_df, x='year', y='wine', title='Потребление вина')
    wine_fig.update_layout(height=350)

    brandy_fig = px.line(filtered_df, x='year', y='brandy', title='Потребление бренди')
    brandy_fig.update_layout(height=350)

    vodka_fig = px.line(filtered_df, x='year', y='vodka', title='Потребление водки')
    vodka_fig.update_layout(height=350)

    champagne_fig = px.line(filtered_df, x='year', y='champagne', title='Потребление шампанского')
    champagne_fig.update_layout(height=350)

    return beer_fig, wine_fig, brandy_fig, vodka_fig, champagne_fig

