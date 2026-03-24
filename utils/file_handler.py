import json
import os
from typing import Any

def load_data(file_path: str, default: Any = None) -> Any:
    """Load data from json file."""
    if not os.path.exists(file_path):
        return default
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return default

def save_data(file_path: str, data: Any) -> None:
    """Save data to json file."""
    os.makedirs(os.path.dirname(file_path) or '.', exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


