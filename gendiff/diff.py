from .file_parser import parse_file


def generate_diff(file_path1, file_path2):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    lines = []

    for key in keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        format_value = lambda v: str(v).lower() if isinstance(v, bool) else str(v)

        if key not in data2:
            lines.append(f"  - {key}: {format_value(val1)}")
        elif key not in data1:
            lines.append(f"  + {key}: {format_value(val2)}")
        elif val1 == val2:
            lines.append(f"    {key}: {format_value(val1)}")
        else:
            lines.append(f"  - {key}: {format_value(val1)}")
            lines.append(f"  + {key}: {format_value(val2)}")

    return "{\n" + "\n".join(lines) + "\n}"
