import about, alcohol_map, dinamic, statistic, top
import dash_bootstrap_components as dbc
from data import df
from dash import Dash, Input, Output, dcc, html


external_stylesheets = [dbc.themes.LUX] 
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "18rem",
    "padding": "2rem 1rem",
    "background-color": "#ffc0cb",
}

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Потребление алкогольных напитков в России", className="display-8"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("О проекте", href="/", active="exact"),
                dbc.NavLink("Карта потребления алкоголя", href="/page-1", active="exact"),
                dbc.NavLink("Динамика потребления напитков", href="/page-2", active="exact"),
                dbc.NavLink("Общая статистика", href="/page-3", active="exact"),
                dbc.NavLink("Топ 10 регионов России", href="/page-4", active="exact")
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])

def render_page_content(pathname):
    if pathname == "/":
        return about.layout
    if pathname == "/page-1":
        return alcohol_map.layout
    elif pathname == "/page-2":
        return dinamic.layout
    elif pathname == "/page-3":
        return statistic.layout
    elif pathname == "/page-4":
         return top.layout
    
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )

if __name__ == '__main__':
        app.run_server(debug=True)
