#!/usr/bin/env python3
"""
Main entry point for the Dash application
Run this file from the root directory: python main.py
"""

import sys
import os
from pathlib import Path

# Add src directory to Python path
src_dir = Path(__file__).parent / "src"
sys.path.insert(0, str(src_dir))

from src.app import create_app

if __name__ == "__main__":
    app, config = create_app()
    print(f"Starting {config.app_name} on http://{config.host}:{config.port}")
    app.run(
        debug=config.debug,
        host=config.host,
        port=config.port
    )