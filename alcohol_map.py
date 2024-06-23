from dash import html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import json
import requests
from data import df

url = 'https://raw.githubusercontent.com/PanamCU/map/main/russia%20copy.geojson'
response = requests.get(url)
counties = response.json()

rusmap = px.choropleth_mapbox(
    df,
    geojson=counties,
    featureidkey='properties.cartodb_id',
    locations='cartodb_id',
    color_continuous_scale=px.colors.sequential.Pinkyl,
    mapbox_style="carto-positron",
    zoom=3,
    opacity=0.5,
    hover_name='region',
    hover_data={'region': True, 'cartodb_id': False},
    labels={'region': 'Субъект РФ'}
)

rusmap.update_layout(
    margin={"r": 0, "t": 0, "l": 0, "b": 0},
    mapbox_zoom=1,
    mapbox_center={"lat": 66, "lon": 94},
    height=500,
    showlegend=False
)

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
            html.H1("Тепловая карта потребления алкоголя"),
            html.P("Анализ потребления алкоголя по регионам России."),
            html.Hr(style={'color': 'black'}),
        ], style={'textAlign': 'center'}))
    ]),

    html.Br(),

    dbc.Row([
        dbc.Col([dbc.Label("Напиток:"),
            dbc.RadioItems(
                options=[
                    {'label':'Вино', 'value': 'wine'},
                    {'label':'Пиво', 'value': 'beer'},
                    {'label':'Водка', 'value': 'vodka'},
                    {'label':'Шампанское', 'value': 'champagne'},
                    {'label':'Бренди', 'value': 'brandy'}
                ],
                value='wine',
                id='crossfilter-ind',
            ),
        ], width=3),

        dbc.Col([
            dcc.Graph(id='choropleth', config={'displayModeBar': False}),
        ], width=9)
    ]),

    dbc.Row([
        dbc.Col([
            dbc.Label("Год:"),
            dcc.Slider(
                id='year-slider',
                min=df['year'].min(),
                max=df['year'].max(),
                value=df['year'].min(),
                marks={str(year): str(year) for year in df['year'].unique()},
                step=None
            )
        ])
    ])
])

@callback(
    Output('choropleth', 'figure'),
    Input('crossfilter-ind', 'value'),
    Input('year-slider', 'value')
)
def update_choropleth(indication, year):
    filtered_df = df[df['year'] == year]

    translation_dict = {
    "wine": "вина",
    "beer": "пива",
    "vodka": "водки",
    "champagne": "шампанского",
    "brandy": "бренди"
    }

    figure = px.choropleth_mapbox(
        filtered_df,
        geojson=counties,
        featureidkey='properties.cartodb_id',
        locations='cartodb_id',
        color=indication,
        color_continuous_scale=px.colors.sequential.Pinkyl,
        mapbox_style="carto-positron",
        zoom=3,
        opacity=0.5,
        hover_name='region',
        hover_data={'region': True, 'cartodb_id': False, indication: True},
        labels={indication: f'Продажи {translation_dict[indication]}, л'}
    )

    figure.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        mapbox_zoom=1,
        mapbox_center={"lat": 66, "lon": 94},
        height=500,
        showlegend=False
    )

    return figure