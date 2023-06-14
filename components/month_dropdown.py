from dash import dcc, html
from dash.dependencies import Input, Output
from .ids import *


def render(app,data):
    all_months = data["month"].unique()

    @app.callback(
        Output(MONTH_DROPDOWN, "value"),
        [
            Input(YEAR_DROPDOWN, "value"),
            Input(SELECT_ALL_MONTHS_BUTTON, "n_clicks")
        ]
    )
    def select_all_months(years, n):
        filtered_data = data.query("year in @years")
        return sorted(filtered_data["month"].unique())

    return html.Div(
            [
                html.H6("Month"),
                dcc.Dropdown(
                    id = MONTH_DROPDOWN,
                    options = [{"label":month, "value":month } for month in all_months],
                    multi=True
                ),
                html.Button(
                    className="dropdown-button",
                    children=["Select All"],
                    id = SELECT_ALL_MONTHS_BUTTON,
                    n_clicks=0
                )
            ]
    )
    