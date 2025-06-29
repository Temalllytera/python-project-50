import os
import pytest
from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)


def read_fixture(filename):
    with open(get_fixture_path(filename)) as f:
        return f.read().strip()


@pytest.mark.parametrize("file_format", ["json", "yml"])
def test_flat_file_diff(file_format):
    file1 = get_fixture_path(f'file1.{file_format}')
    file2 = get_fixture_path(f'file2.{file_format}')
    expected = read_fixture('expected_flat.txt')
    assert generate_diff(file1, file2) == expected
