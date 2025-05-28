#!/usr/bin/env python3
import argparse
from pathlib import Path
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        add_help=False
    )

    parser.add_argument('first_file', type=Path, help='Path to the first file')
    parser.add_argument('second_file', type=Path, help='Path to the second file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish'
    )
    parser.add_argument('-h', '--help', action='help', help='show this help message and exit')

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
    