import pandas as pd
import os
from typing import Optional, Union, Dict, Any

class DataHandler:
    """Handle data loading and processing"""
    
    def __init__(self, data_path: str = "data/"):
        self.data_path = data_path
        self._cache = {}
    
    def load_csv(self, filename: str, use_cache: bool = True) -> pd.DataFrame:
        """Load CSV file with caching"""
        if use_cache and filename in self._cache:
            return self._cache[filename]
        
        filepath = os.path.join(self.data_path, filename)
        df = pd.read_csv(filepath)
        
        if use_cache:
            self._cache[filename] = df
        
        return df
    
    def process_data(self, df: pd.DataFrame, operations: Dict[str, Any]) -> pd.DataFrame:
        """Apply data processing operations"""
        processed_df = df.copy()
        
        for operation, params in operations.items():
            if operation == "filter":
                processed_df = processed_df.query(params)
            elif operation == "sort":
                processed_df = processed_df.sort_values(params)
            elif operation == "group":
                processed_df = processed_df.groupby(params["by"]).agg(params["agg"])
        
        return processed_df