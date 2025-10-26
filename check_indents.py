#!/usr/bin/env python3
import difflib
from pathlib import Path

# Импортируй свою функцию генерации диффа:
from gendiff import generate_diff  # ← поменяй путь, если у тебя модуль иначе называется

# Пути к тестовым файлам
FIXTURES_DIR = Path('tests/fixtures')
EXPECTED_FILE = FIXTURES_DIR / 'expected_nested_stylish.txt'


def compare_output(file_format: str):
    """Сравнивает expected и результат generate_diff"""
    file1 = FIXTURES_DIR / f'file1_nested.{file_format}'
    file2 = FIXTURES_DIR / f'file2_nested.{file_format}'

    expected = EXPECTED_FILE.read_text().strip()
    actual = generate_diff(file1, file2, 'stylish').strip()

    if expected == actual:
        print(f'✅ {file_format.upper()} — совпадает с ожидаемым!\n')
        return

    print(f'\n❌ Различия для {file_format.upper()}:\n')
    diff = difflib.unified_diff(
        expected.splitlines(),
        actual.splitlines(),
        fromfile='expected',
        tofile='actual',
        lineterm=''
    )
    for line in diff:
        print(line)


def main():
    compare_output('json')
    compare_output('yml')


if __name__ == '__main__':
    main()
