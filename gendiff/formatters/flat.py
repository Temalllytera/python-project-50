def format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return str(value)


def format_flat(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    lines = []

    for key in keys:
        if key not in data2:
            lines.append(f"  - {key}: {format_value(data1[key])}")
        elif key not in data1:
            lines.append(f"  + {key}: {format_value(data2[key])}")
        elif data1[key] == data2[key]:
            lines.append(f"    {key}: {format_value(data1[key])}")
        else:
            lines.append(f"  - {key}: {format_value(data1[key])}")
            lines.append(f"  + {key}: {format_value(data2[key])}")

    return "{\n" + "\n".join(lines) + "\n}"
