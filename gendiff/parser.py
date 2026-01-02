import json
import yaml
from pathlib import Path


def parse_file(file_path):
    path = Path(file_path)

    with open(path) as f:
        if path.suffix == '.json':
            return json.load(f)
        if path.suffix in ('.yaml', '.yml'):
            return yaml.safe_load(f)

    raise ValueError(f"Unsupported file format: {path.suffix}")
