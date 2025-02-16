def format_value(value, level):
    if isinstance(value, dict):
        lines = ['{']
        for k, v in value.items():
            lines.append(f"{' ' * (level + 4)}{k}: {format_value(v, level + 4)}")
        lines.append(f"{' ' * level}}}")
        return '\n'.join(lines)

    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def format_stylish(diff, level=0):
    lines = ['{']
    for key, node in sorted(diff.items()):
        status = node['status']

        if status == 'nested':
            lines.append(f"{' ' * (level + 2)}  {key}: {format_stylish(node['children'], level + 4)}")
        elif status == 'added':
            lines.append(f"{' ' * (level + 2)}+ {key}: {format_value(node['value'], level + 4)}")
        elif status == 'removed':
            lines.append(f"{' ' * (level + 2)}- {key}: {format_value(node['value'], level + 4)}")
        elif status == 'changed':
            lines.append(f"{' ' * (level + 2)}- {key}: {format_value(node['old'], level + 4)}")
            lines.append(f"{' ' * (level + 2)}+ {key}: {format_value(node['new'], level + 4)}")
        else:
            lines.append(f"{' ' * (level + 2)}  {key}: {format_value(node['value'], level + 4)}")

    lines.append(f"{' ' * level}}}")
    return '\n'.join(lines)
