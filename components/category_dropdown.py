from dash import dcc, html
from dash.dependencies import Input, Output
from .ids import *


def render(app,data):
    all_categories = data["category"].unique()

    @app.callback(
        Output(CATEGORY_DROPDOWN, "value"),
        [
            Input(YEAR_DROPDOWN, "value"),
            Input(MONTH_DROPDOWN, "value"),
            Input(SELECT_ALL_CATEGORIES_BUTTON, "n_clicks")
        ]
    )
    def select_all_months(years, months, n):
        filtered_data = data.query("year in @years and month in @months")
        return sorted(filtered_data["category"].unique())

    return html.Div(
            [
                html.H6("Category"),
                dcc.Dropdown(
                    id = CATEGORY_DROPDOWN,
                    options = [{"label":c, "value":c } for c in all_categories],
                    multi=True
                ),
                html.Button(
                    className="dropdown-button",
                    children=["Select All"],
                    id = SELECT_ALL_CATEGORIES_BUTTON,
                    n_clicks=0
                )
            ]
    )
    