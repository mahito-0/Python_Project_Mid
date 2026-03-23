import json
import os
from typing import Any

def save_data(file_path: str, data: Any) -> None:
    """Save data to json file."""
    os.makedirs(os.path.dirname(file_path) or '.', exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


