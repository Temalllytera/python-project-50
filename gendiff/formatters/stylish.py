def stringify(value, depth):
    """Convert value to string with proper formatting."""
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    if not isinstance(value, dict):
        # Для пустых строк возвращаем пустую строку (без пробела)
        return "" if value == "" else str(value)

    indent_size = 4
    current_indent = ' ' * (depth * indent_size)
    bracket_indent = ' ' * ((depth + 1) * indent_size)
    lines = ['{']
    for key, val in value.items():
        formatted_value = stringify(val, depth + 1)
        lines.append(f"{bracket_indent}{key}: {formatted_value}")
    lines.append(f"{current_indent}}}")
    return '\n'.join(lines)


def format_stylish(diff, depth=0):
    """Format diff tree to stylish format."""
    indent_size = 4
    current_indent = ' ' * (depth * indent_size)

    # Ключевая формула: для элементов со знаками отступ = depth * 4 + 2
    # Для элементов без знаков: depth * 4 + 4
    sign_indent = ' ' * (depth * indent_size + 2)
    no_sign_indent = ' ' * (depth * indent_size + 4)

    lines = ['{']

    for node in diff:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            children = format_stylish(node['children'], depth + 1)
            lines.append(f"{no_sign_indent}{key}: {children}")
        elif node_type == 'added':
            value = stringify(node['value'], depth + 1)
            lines.append(f"{sign_indent}+ {key}: {value}")
        elif node_type == 'removed':
            value = stringify(node['value'], depth + 1)
            lines.append(f"{sign_indent}- {key}: {value}")
        elif node_type == 'changed':
            old_value = stringify(node['old_value'], depth + 1)
            new_value = stringify(node['new_value'], depth + 1)
            lines.append(f"{sign_indent}- {key}: {old_value}")
            lines.append(f"{sign_indent}+ {key}: {new_value}")
        elif node_type == 'unchanged':
            value = stringify(node['value'], depth + 1)
            lines.append(f"{no_sign_indent}{key}: {value}")

    lines.append(f"{current_indent}}}")
    return '\n'.join(lines)
