def build_diff_tree(data1, data2):
    keys = sorted(set(data1) | set(data2))
    diff = []

    for key in keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key not in data2:
            diff.append({
                'key': key,
                'type': 'removed',
                'value': value1,
            })
        elif key not in data1:
            diff.append({
                'key': key,
                'type': 'added',
                'value': value2,
            })
        elif value1 == value2:
            diff.append({
                'key': key,
                'type': 'unchanged',
                'value': value1,
            })
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append({
                'key': key,
                'type': 'nested',
                'children': build_diff_tree(value1, value2),
            })
        else:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': value1,
                'new_value': value2,
            })

    return diff
