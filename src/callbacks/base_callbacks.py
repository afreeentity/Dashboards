from dash import Input, Output, callback
import pandas as pd
from utils.data_handler import DataHandler

def register_base_callbacks(app):
    """Register base callbacks for the application"""
    
    @app.callback(
        Output('page-content', 'children'),
        Input('url', 'pathname')
    )
    def display_page(pathname):
        if pathname == '/':
            return create_dashboard_page()
        elif pathname == '/data':
            return create_data_page()
        elif pathname == '/viz':
            return create_viz_page()
        elif pathname == '/reports':
            return create_reports_page()
        else:
            return create_404_page()

def create_dashboard_page():
    """Create dashboard home page"""
    from dash import html, dcc
    import plotly.graph_objs as go
    
    return html.Div([
        html.H2("Dashboard Overview"),
        html.Div([
            html.Div([
                html.H4("Sample Metric"),
                html.H2("1,234", className="text-primary")
            ], className="text-center", style={"padding": "20px", "border": "1px solid #ddd"})
        ])
    ])

def create_data_page():
    """Create data view page"""
    from dash import html, dash_table
    
    return html.Div([
        html.H2("Data View"),
        html.Div(id="data-table-container")
    ])

def create_viz_page():
    """Create visualization page"""
    from dash import html, dcc
    
    return html.Div([
        html.H2("Visualizations"),
        dcc.Graph(id="sample-chart")
    ])

def create_reports_page():
    """Create reports page"""
    from dash import html
    
    return html.Div([
        html.H2("Reports"),
        html.P("Reports functionality coming soon...")
    ])

def create_404_page():
    """Create 404 error page"""
    from dash import html
    
    return html.Div([
        html.H1("404: Page not found"),
        html.P("The page you're looking for doesn't exist.")
    ])