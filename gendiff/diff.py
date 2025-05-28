def generate_diff(file_path1, file_path2):
    import json

    with open(file_path1) as f1, open(file_path2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    lines = []

    for key in keys:
        if key not in data2:
            lines.append(f"  - {key}: {data1[key]}")
        elif key not in data1:
            lines.append(f"  + {key}: {data2[key]}")
        elif data1[key] == data2[key]:
            lines.append(f"    {key}: {data1[key]}")
        else:
            lines.append(f"  - {key}: {data1[key]}")
            lines.append(f"  + {key}: {data2[key]}")

    return "{\n" + "\n".join(lines) + "\n}"
