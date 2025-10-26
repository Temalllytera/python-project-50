import os
import pytest
from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)


def read_fixture(filename):
    with open(get_fixture_path(filename), 'r') as f:
        return f.read().strip()


@pytest.mark.parametrize("file_format", ["json", "yml"])
def test_flat_file_diff(file_format):
    file1 = get_fixture_path(f'file1.{file_format}')
    file2 = get_fixture_path(f'file2.{file_format}')
    expected = read_fixture('expected_flat.txt')

    assert generate_diff(file1, file2, 'flat') == expected


@pytest.mark.parametrize("file_format", ["json", "yml"])
def test_nested_stylish_diff(file_format):
    file1 = get_fixture_path(f'file1_nested.{file_format}')
    file2 = get_fixture_path(f'file2_nested.{file_format}')
    expected = read_fixture('expected_nested_stylish.txt')

    result = generate_diff(file1, file2, 'stylish').strip()
    expected = expected.strip()
    assert result == expected

    result_default = generate_diff(file1, file2).strip()
    assert result_default == expected


@pytest.mark.parametrize("file_format", ["json", "yml"])
def test_nested_plain_diff(file_format):
    file1 = get_fixture_path(f'file1_nested.{file_format}')
    file2 = get_fixture_path(f'file2_nested.{file_format}')
    expected = read_fixture('expected_nested_plain.txt')

    result = generate_diff(file1, file2, 'plain')
    assert result == expected


@pytest.mark.parametrize("file_format", ["json", "yml"])
def test_nested_json_diff(file_format):
    file1 = get_fixture_path(f'file1_nested.{file_format}')
    file2 = get_fixture_path(f'file2_nested.{file_format}')
    expected = read_fixture('expected_nested_json.txt')

    result = generate_diff(file1, file2, 'json')
    assert result == expected


def test_error_handling():
    with pytest.raises(ValueError, match="File not found"):
        generate_diff("not_exist.json", get_fixture_path('file2.json'))

    with pytest.raises(ValueError, match="Unsupported format"):
        generate_diff(
            get_fixture_path('file1.json'),
            get_fixture_path('file2.json'),
            'unknown_format'
        )

    with pytest.raises(ValueError, match="Unsupported file format"):
        invalid_file = get_fixture_path('invalid.txt')
        with open(invalid_file, 'w') as f:
            f.write("dummy content")
        try:
            generate_diff(invalid_file, get_fixture_path('file2.json'))
        finally:
            if os.path.exists(invalid_file):
                os.remove(invalid_file)


def test_format_selection():
    file1 = get_fixture_path('file1_nested.json')
    file2 = get_fixture_path('file2_nested.json')

    stylish_result = generate_diff(file1, file2, 'stylish')
    plain_result = generate_diff(file1, file2, 'plain')
    flat_result = generate_diff(file1, file2, 'flat')
    json_result = generate_diff(file1, file2, 'json')

    assert stylish_result != plain_result
    assert stylish_result != flat_result
    assert stylish_result != json_result
    assert plain_result != flat_result
    assert plain_result != json_result
    assert flat_result != json_result

    # Проверяем что JSON валиден
    import json
    parsed = json.loads(json_result)
    assert isinstance(parsed, list)

    # Проверяем структуру JSON
    assert len(parsed) > 0
    for item in parsed:
        assert 'key' in item
        assert 'type' in item
        