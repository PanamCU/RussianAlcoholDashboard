from dash import html, dcc
import dash_bootstrap_components as dbc
from data import df

layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.Div([
            html.H2("Описание проекта"),
            html.Hr(style={'color': 'black'}),
        ], style={'textAlign': 'center', 'marginBottom': '20px'}))
    ]),
    dbc.Row([
        dbc.Col(html.Div([
            html.H5("Общая информация о датасете"),
            html.P(
                "Данный датасет содержит информацию о потреблении различных видов алкогольных напитков в разных регионах России за период с 1998 по 2016 год. "
                "Данные включают год, регион, а также количество потребленного вина, пива, водки, шампанского и бренди. "
                "Датасет был модернизирован, в следствие чего в него была добавлена информация о рождаемости, смертности и урбанизации. "
            ),
            dbc.Button("Скачать датасет", color="primary", href="https://docs.google.com/spreadsheets/d/e/2PACX-1vTTYt1uMLU8_Tj0jtrBjdaz1I0U4y_2m4vHGjLJ8OWStP9AuntfQfd00D8zvkcit93OK5ysSIBTlSY2/pub?gid=1669335283&single=true&output=csv", target="_blank"),
            html.P(" "),
            html.Hr(style={'color': 'black'}),
            html.H5("Общая информация о дашборде"),
            html.P(
                "На дашборде представлено 4 страницы, с разнообразными графиками."
            ),
            html.P(
                "На первой странице находится тепловая карта России. Слева от карты присутствуют показатели, выбрав которые, можно увидеть потребление алкогольных напитков по регионам России. "
                "Также, под картой находится ползунок, на котором можно выбрать год, что позволит более точно проанализировать информацию."
            ),
            html.P(
                "На второй странице представлены 5 линейных диаграмм, каждая из которых относится к своему напитку, и в точности отражает его потребление на протяжении 18 лет, в зависимости от выбранного региона. "
                "Данные графики специально были выполнены отдельно, чтобы наглядно показать изменения в потреблении каждого напитка отдельно."
            ),
            html.P(
                "На третьей странице присутствует 3 диаграммы: столбчатая, круговая и пузырьковая. "
                "На столбчатой диаграмме представлена общая статистика по потреблению алкогольных напитков на протяжении 18 лет. "
                "На круговой диаграмме - отношение потребления алкогольных напитков в процентах (присутствует выбор по годам). "
                "На пузырьковой диаграмме представлено отношение рождаемости к смертности по годам."
            ),
            html.P(
                "На четвертой странице преимущественно сравниваются все регионы по таким показателям как урбанизация, потребление алкоголя, рождаемость и смертность. "
                "Для удобства сравнения были представлены топ 10 регионов по данным показателям. "
                "Также, на этой странице присутствует горизонтальная столбчатая диаграмма, со средними показателями выпитого алкоголя по всей России за выбранный год"
            ),
            html.Hr(style={'color': 'black'}),
            html.H5("Репозиторий GitHub"),
            html.P(
                "Полный код данного дашборда Вы можете найти по кнопке ниже."
            ),
            dbc.Button("Перейти к репозиторию на GitHub", color="primary", href="https://github.com/PanamCU/RussianAlcoholDashboard", target="_blank"),
        ]), width=12)
    ])
], style={'padding': '20px'})