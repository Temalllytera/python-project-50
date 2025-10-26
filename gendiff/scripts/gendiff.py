#!/usr/bin/env python3
import argparse
from pathlib import Path
from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        add_help=False
    )

    parser.add_argument(
        'first_file',
        type=Path,
        help='Path to the first configuration file'
    )

    parser.add_argument(
        'second_file',
        type=Path,
        help='Path to the second configuration file'
    )

    parser.add_argument(
        '-f', '--format',
        help='Set output format (default: stylish)',
        default='stylish',
        choices=['stylish', 'flat', 'plain', 'json'],
        metavar='FORMAT'
    )

    parser.add_argument(
        '-h', '--help',
        action='help',
        help='Show this help message and exit'
    )

    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
