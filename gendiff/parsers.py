import json
import yaml
from pathlib import Path


def parse_file(file_path):
    path = Path(file_path)
    extension = path.suffix.lower()

    if extension in ('.json'):
        return parse_json(file_path)
    elif extension in ('.yaml', '.yml'):
        return parse_yaml(file_path)
    else:
        raise ValueError(f"Unsupported file format: {extension}")


def parse_json(file_path):
    with open(file_path) as f:
        return json.load(f)


def parse_yaml(file_path):
    with open(file_path) as f:
        return yaml.safe_load(f)
