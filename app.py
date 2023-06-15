from dash import Dash
import dash_bootstrap_components as dbc 
from layout import create_layout
from data.util import get_data
import os

cwd = os.getcwd()
file_path = (f'{cwd}/data/gas_sale.csv')


# def App():
data = get_data(file_path)
app = Dash(external_stylesheets=[dbc.themes.LUMEN])
server = app.server
app.title = 'Gas Prices'
app.layout = create_layout(app, data)
app.run_server(debug=True)




# App()