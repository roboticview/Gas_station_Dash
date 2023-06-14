import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from .ids import *


def render(app,data):
    @app.callback(
        Output(PIE_CHART, "children"),
        [
            Input(YEAR_DROPDOWN, "value"),
            Input(MONTH_DROPDOWN, "value"),
            Input(CATEGORY_DROPDOWN, "value")
        ]
    )
    def update_pie_chart(years, months, categories):
        print(data)
        filtered_data = data.query(
            "year in @years and month in @months  and category in @categories"
        )
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected", id=PIE_CHART)

        fig = px.pie(filtered_data, values="amount", names="category",hole = 0.4)
        return html.Div(dcc.Graph(figure=fig), id=PIE_CHART)
    return html.Div(id=PIE_CHART)