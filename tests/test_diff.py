import json
import os
import pytest
from gendiff import generate_diff


FIXTURES_DIR = os.path.join(os.path.dirname(__file__), 'fixtures')


def fixture_path(name):
    return os.path.join(FIXTURES_DIR, name)


def read_fixture(name):
    with open(fixture_path(name), 'r') as f:
        return f.read().strip()


# ---------- BASIC FUNCTIONALITY ----------

@pytest.mark.parametrize("ext", ["json", "yml"])
def test_flat_diff_stylish(ext):
    file1 = fixture_path(f"file1.{ext}")
    file2 = fixture_path(f"file2.{ext}")
    expected = read_fixture("expected_flat.txt")

    result = generate_diff(file1, file2)
    assert result.strip() == expected.strip()


# ---------- NESTED STRUCTURES ----------

@pytest.mark.parametrize("ext", ["json", "yml"])
def test_nested_diff_stylish(ext):
    file1 = fixture_path(f"file1_nested.{ext}")
    file2 = fixture_path(f"file2_nested.{ext}")
    expected = read_fixture("expected_nested_stylish.txt")

    result = generate_diff(file1, file2, "stylish")
    assert result.strip() == expected.strip()


@pytest.mark.parametrize("ext", ["json", "yml"])
def test_nested_diff_plain(ext):
    file1 = fixture_path(f"file1_nested.{ext}")
    file2 = fixture_path(f"file2_nested.{ext}")
    expected = read_fixture("expected_nested_plain.txt")

    result = generate_diff(file1, file2, "plain")
    assert result.strip() == expected.strip()


# ---------- JSON FORMAT ----------

@pytest.mark.parametrize("ext", ["json", "yml"])
def test_json_output_is_valid_json(ext):
    file1 = fixture_path(f"file1_nested.{ext}")
    file2 = fixture_path(f"file2_nested.{ext}")

    result = generate_diff(file1, file2, "json")

    parsed = json.loads(result)
    assert isinstance(parsed, list)
    assert len(parsed) > 0

    for node in parsed:
        assert "key" in node
        assert "type" in node


# ---------- FORMAT SELECTION ----------

def test_different_formats_produce_different_outputs():
    file1 = fixture_path("file1_nested.json")
    file2 = fixture_path("file2_nested.json")

    stylish = generate_diff(file1, file2, "stylish")
    plain = generate_diff(file1, file2, "plain")
    json_output = generate_diff(file1, file2, "json")

    assert stylish != plain
    assert stylish != json_output
    assert plain != json_output


# ---------- ERROR HANDLING (CONTRACT-LEVEL) ----------

def test_error_on_missing_file():
    with pytest.raises(Exception):
        generate_diff("not_existing_file.json", fixture_path("file2.json"))


def test_error_on_unknown_format():
    with pytest.raises(Exception):
        generate_diff(
            fixture_path("file1.json"),
            fixture_path("file2.json"),
            "unknown"
        )
