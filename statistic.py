from dash import html, dcc, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from data import df

all_regions = df['region'].unique()
all_years = df['year'].unique()

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
            html.H3("Общая статистика по потреблению аклогольных напитков"),
            html.Hr(style={'color': 'black'}),
        ], style={'textAlign': 'center'}))
    ]),
    dbc.Row([
        dbc.Col([
            html.P("Регион:"),
            dcc.Dropdown(
                id='region-dropdown-2',
                options=[{'label': region, 'value': region} for region in all_regions],
                value=all_regions[0]
            )
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='alcohol-consumption-graph'), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.P("Год:"),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': year, 'value': year} for year in all_years],
                value=all_years[-1]
            )
        ], width=6)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='alcohol-consumption-pie-chart'), width=6),
        dbc.Col(dcc.Graph(id='birth-death-rate-scatter'), width=6)
    ])
])

@callback(
    [Output('alcohol-consumption-graph', 'figure'),
     Output('alcohol-consumption-pie-chart', 'figure'),
     Output('birth-death-rate-scatter', 'figure')],
    [Input('region-dropdown-2', 'value'),
     Input('year-dropdown', 'value')]
)
def update_demographic_graphs(selected_region, selected_year):
    filtered_df = df[df['region'] == selected_region]

    alcohol_consumption_fig = px.bar(filtered_df, x='year', y=['wine', 'beer', 'vodka', 'champagne', 'brandy'],
                                     title='Потребление алкоголя на протяжении 18-ти лет', barmode='group')
    alcohol_consumption_fig.update_layout(height=370)

    latest_data = filtered_df[filtered_df['year'] == selected_year]
    alcohol_pie_data = latest_data[['wine', 'beer', 'vodka', 'champagne', 'brandy']].melt(var_name='alcohol', value_name='consumption')
    alcohol_consumption_pie_chart = px.pie(alcohol_pie_data, names='alcohol', values='consumption', title=f'Потребление алкоголя в {selected_year}')
    alcohol_consumption_pie_chart.update_layout(height=350)

    filtered_df = filtered_df.sort_values(by='death_rate')
    birth_death_rate_scatter = px.scatter(filtered_df, x='birth_rate', y='death_rate', size='urbanization', color='year',
                                          title='Отношение рождаемости к смертности', labels={'birth_rate': 'Birth Rate', 'death_rate': 'Death Rate', 'urbanization': 'Urbanization'})
    birth_death_rate_scatter.update_layout(height=350)

    return alcohol_consumption_fig, alcohol_consumption_pie_chart, birth_death_rate_scatter