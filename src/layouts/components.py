from dash import dcc, html
import dash_bootstrap_components as dbc

def create_header():
    """Create application header"""
    return dbc.Navbar([
        dbc.NavbarBrand("Dashboard Template", href="/"),
        dbc.Nav([
            dbc.NavLink("Home", href="/", active="exact"),
            dbc.NavLink("Analytics", href="/analytics", active="exact"),
            dbc.NavLink("Settings", href="/settings", active="exact"),
        ], navbar=True)
    ], color="primary", dark=True, className="mb-3")

def create_sidebar():
    """Create sidebar with navigation"""
    return dbc.Card([
        dbc.CardHeader("Navigation"),
        dbc.CardBody([
            dbc.Nav([
                dbc.NavLink("Dashboard", href="/", active="exact"),
                dbc.NavLink("Data View", href="/data", active="exact"),
                dbc.NavLink("Visualizations", href="/viz", active="exact"),
                dbc.NavLink("Reports", href="/reports", active="exact"),
            ], vertical=True, pills=True)
        ])
    ])

def create_main_content():
    """Create main content area"""
    return html.Div(id="page-content", children=[
        html.H1("Welcome to Dashboard Template"),
        html.P("Select a page from the sidebar to get started.")
    ])