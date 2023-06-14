from dash import Dash,html
import dash_bootstrap_components as dbc
from components import (
                pie_chart, 
                year_dropdown,
                month_dropdown,
                category_dropdown,
            )

def create_layout(app,data):
    heading = html.H1(
        'Gas Prices',
        className = 'bg-primary text-secondary p-2 mb-3'
    )
    return dbc.Container([
        dbc.Row([
            dbc.Col(heading)
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(
                [
                    year_dropdown.render(app,data), 
                    month_dropdown.render(app,data),
                    category_dropdown.render(app,data)
                ],
                className="dropdown-container"
                ),lg= 6),
            dbc.Col(pie_chart.render(app,data), lg =6),
        ]),
     ])