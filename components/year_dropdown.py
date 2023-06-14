from dash import Dash, html, dcc
from .ids import *
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


def render(app,data):
    all_years = data['year'].unique()

    @app.callback(
        Output(YEAR_DROPDOWN, "value"),
        Input(SELECT_ALL_YEARS_BUTTON, "n_clicks")
    )
    def select_all_years(n):
        return all_years

    dropdown = html.Div(
        [
            html.H6("Year"),
            dcc.Dropdown(
                id=YEAR_DROPDOWN,
                options=[{"label":year, "value":year} for year in all_years],
                multi=True,
            ),
            html.Button(
                id=SELECT_ALL_YEARS_BUTTON,
                children=["Select All"],
                className="dropdown-button",
                n_clicks=0
                ),
        ]
    )
    return dropdown