from gendiff.parsers import parse_file


def build_diff(data1, data2):
    diff = {}
    keys = sorted(data1.keys() | data2.keys())

    for key in keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if key not in data2:
            diff[key] = {'status': 'removed', 'value': val1}
        elif key not in data1:
            diff[key] = {'status': 'added', 'value': val2}
        elif isinstance(val1, dict) and isinstance(val2, dict):
            diff[key] = {'status': 'nested', 'children': build_diff(val1, val2)}
        elif val1 == val2:
            diff[key] = {'status': 'unchanged', 'value': val1}
        else:
            diff[key] = {'status': 'changed', 'old': val1, 'new': val2}

    return diff
