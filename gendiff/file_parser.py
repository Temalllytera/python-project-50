import json
import yaml
from pathlib import Path


def parse_file(file_path):
    path = Path(file_path)
    suffix = path.suffix.lower()

    with open(file_path, 'r') as f:
        if suffix == '.json':
            return json.load(f)
        elif suffix in ('.yaml', '.yml'):
            return yaml.safe_load(f)
        else:
            raise ValueError(f"Unsupported file format: {suffix}")
