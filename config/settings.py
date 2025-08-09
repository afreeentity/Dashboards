import os
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class DashConfig:
    """Base configuration for Dash applications"""
    app_name: str = "Dash Template"
    debug: bool = True
    host: str = "127.0.0.1"
    port: int = 8050
    
    # Styling
    external_stylesheets: list = None
    external_scripts: list = None
    
    # Data
    data_path: str = "data/"
    
    def __post_init__(self):
        if self.external_stylesheets is None:
            self.external_stylesheets = [
                "https://codepen.io/chriddyp/pen/bWLwgP.css"
            ]

def get_config() -> DashConfig:
    """Get configuration based on environment"""
    return DashConfig()