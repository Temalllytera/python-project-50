import json


def generate_diff(filepath1, filepath2, output_format='stylish'):
    data1 = _read_json(filepath1)
    data2 = _read_json(filepath2)

    diff_lines = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        if key in data1 and key not in data2:
            diff_lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1 and key in data2:
            diff_lines.append(f"  + {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            diff_lines.append(f"    {key}: {data1[key]}")
        else:
            diff_lines.append(f"  - {key}: {data1[key]}")
            diff_lines.append(f"  + {key}: {data2[key]}")

    result = "{\n" + "\n".join(diff_lines) + "\n}"
    return result


def _read_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)
