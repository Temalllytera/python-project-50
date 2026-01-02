from .formatters import flat, json, plain, stylish
from .parser import parse_file
from .tree_builder import build_diff_tree


def generate_diff(file_path1, file_path2, format_name="stylish"):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)

    diff_tree = build_diff_tree(data1, data2)

    if format_name == "stylish":
        return stylish.format_stylish(diff_tree)
    if format_name == "flat":
        return flat.format_flat(diff_tree)
    if format_name == "plain":
        return plain.format_plain_output(diff_tree)
    if format_name == "json":
        return json.format_json(diff_tree)

    raise ValueError(f"Unsupported format: {format_name}")
