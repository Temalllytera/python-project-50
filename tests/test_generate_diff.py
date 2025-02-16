import pytest
from gendiff.core import generate_diff


@pytest.mark.parametrize("format", ["json", "yml"])
def test_generate_diff(format):
    file1 = f"tests/test_data/file1.{format}"
    file2 = f"tests/test_data/file2.{format}"

    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

    assert generate_diff(file1, file2) == expected
