from dash import dcc, html
import dash_bootstrap_components as dbc
from .components import create_header, create_sidebar, create_main_content

def create_base_layout():
    """Create the base layout structure"""
    return dbc.Container([
        dcc.Location(id='url', refresh=False),
        create_header(),
        dbc.Row([
            dbc.Col(create_sidebar(), width=3),
            dbc.Col(create_main_content(), width=9)
        ]),
        dcc.Store(id='app-state', data={}),
        dcc.Store(id='data-store', data={})
    ], fluid=True)