import json
import yaml
from pathlib import Path


def parse_file(file_path):
    path = Path(file_path)
    suffix = path.suffix.lower()

    try:
        with open(file_path) as f:
            if suffix == '.json':
                return json.load(f)
            elif suffix in ('.yaml', '.yml'):
                return yaml.safe_load(f)
            raise ValueError(f"Unsupported file format: {suffix}")
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")
    except (json.JSONDecodeError, yaml.YAMLError) as e:
        raise ValueError(f"Error parsing {file_path}: {str(e)}")
