def build_diff_tree(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        node = {'key': key}
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key not in data2:
            node['type'] = 'removed'
            node['value'] = value1
        elif key not in data1:
            node['type'] = 'added'
            node['value'] = value2
        elif isinstance(value1, dict) and isinstance(value2, dict):
            node['type'] = 'nested'
            node['children'] = build_diff_tree(value1, value2)
        elif value1 == value2:
            node['type'] = 'unchanged'
            node['value'] = value1
        else:
            node['type'] = 'changed'
            node['old_value'] = value1
            node['new_value'] = value2

        diff.append(node)

    return diff
