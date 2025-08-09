import sys
import os
from pathlib import Path

# Add the parent directory to Python path so we can import from config
parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(parent_dir))

import dash
from dash import dcc, html
from config.settings import get_config
from src.layouts.base_layout import create_base_layout
from src.callbacks.base_callbacks import register_base_callbacks

def create_app(config=None):
    """Factory function to create Dash app"""
    if config is None:
        config = get_config()
    
    app = dash.Dash(
        __name__,
        external_stylesheets=config.external_stylesheets,
        external_scripts=config.external_scripts,
        suppress_callback_exceptions=True
    )
    
    # Set app title
    app.title = config.app_name
    
    # Create layout
    app.layout = create_base_layout()
    
    # Register callbacks
    register_base_callbacks(app)
    
    return app, config

if __name__ == "__main__":
    app, config = create_app()
    app.run(
        debug=config.debug,
        host=config.host,
        port=config.port
    )