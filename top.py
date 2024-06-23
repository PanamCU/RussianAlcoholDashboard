from dash import html, dcc, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from data import df

df['total_alcohol'] = df[['wine', 'beer', 'vodka', 'champagne', 'brandy']].sum(axis=1)

df['urbanization'] = pd.to_numeric(df['urbanization'], errors='coerce')
df['birth_rate'] = pd.to_numeric(df['birth_rate'], errors='coerce')
df['death_rate'] = pd.to_numeric(df['death_rate'], errors='coerce')

all_regions = df['region'].unique()
all_years = df['year'].unique()

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
            html.H1("Топ 10 регионов по разным показателям"),
            html.P("Сравнение регионов по урбанизации, рождаемости, смертности и потреблению алкоголя."),
            html.Hr(style={'color': 'black'}),
        ], style={'textAlign': 'center'}))
    ]),
    dbc.Row([
        dbc.Col(html.P("Год:"), width="auto"),
        dbc.Col(
            dcc.Dropdown(
                id='year-dropdown-3',
                options=[{'label': year, 'value': year} for year in all_years],
                value=all_years[-1]
            ), width=11
        )
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='top-urbanization-bar'), width=12)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='top-regions-pie-chart'), width=6),
        dbc.Col(dcc.Graph(id='average-indicators-bar'), width=6)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='urbanization-vs-alcohol-scatter'), width=12)
    ])
])

@callback(
    [Output('top-regions-pie-chart', 'figure'),
     Output('average-indicators-bar', 'figure'),
     Output('top-urbanization-bar', 'figure'),
     Output('urbanization-vs-alcohol-scatter', 'figure')],
    [Input('year-dropdown-3', 'value')]
)
def update_graphs(selected_year):
    filtered_df = df[df['year'] == selected_year]

    top_regions = filtered_df[['region', 'total_alcohol']].nlargest(10, 'total_alcohol')
    top_regions_pie_chart = px.pie(top_regions, names='region', values='total_alcohol', title='Топ 10 регионов по потреблению алкоголя')
    top_regions_pie_chart.update_layout(height=380)

    avg_indicators = filtered_df[['wine', 'beer', 'vodka', 'champagne', 'brandy']].mean().reset_index()
    avg_indicators.columns = ['alcohol', 'average']
    average_indicators_bar = px.bar(avg_indicators, x='average', y='alcohol', orientation='h', title='Средние показатели по России за выбранный год')
    average_indicators_bar.update_layout(height=365)

    top_urbanization = filtered_df[['region', 'urbanization', 'birth_rate', 'death_rate']].nlargest(10, 'urbanization')
    top_urbanization_bar = px.bar(top_urbanization.melt(id_vars='region', value_vars=['urbanization', 'birth_rate', 'death_rate']),
                                  x='region', y='value', color='variable', barmode='group',
                                  title='Топ 10 регионов по урбанизации, включая рождаемость и смертность')
    top_urbanization_bar.update_layout(height=400)

    top_urbanization = top_urbanization.merge(filtered_df[['region', 'total_alcohol']], on='region')

    scatter_urbanization_alcohol = px.scatter(
        top_urbanization,
        x='urbanization',
        y='total_alcohol',
        text='region',
        title='Урбанизация vs Потребление алкоголя в топ 10 регионах по урбанизации',
        labels={'urbanization': 'Урбанизация', 'total_alcohol': 'Потребление алкоголя'}
    )
    scatter_urbanization_alcohol.update_traces(marker=dict(size=12), textposition='top center')
    scatter_urbanization_alcohol.update_layout(height=400)

    return top_regions_pie_chart, average_indicators_bar, top_urbanization_bar, scatter_urbanization_alcohol