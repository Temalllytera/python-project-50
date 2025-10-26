def format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def format_plain(diff, path=''):
    lines = []

    for node in diff:
        current_path = f"{path}.{node['key']}" if path else node['key']

        if node['type'] == 'nested':
            lines.extend(format_plain(node['children'], current_path))
        elif node['type'] == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{current_path}' was added with value: {value}")
        elif node['type'] == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node['type'] == 'changed':
            old_value = format_value(node['old_value'])
            new_value = format_value(node['new_value'])
            lines.append(f"Property '{current_path}' was updated. From {old_value} to {new_value}")

    return lines


def format_plain_output(diff):
    lines = format_plain(diff)
    return '\n'.join(lines)