import argparse

from gendiff.core import generate_diff


def main():

    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file', type=str, help="First file path")
    parser.add_argument('second_file', type=str, help="Second file path")
    parser.add_argument(
        '-f', '--format',
        type=str,
        default='stylish',
        help="set format of output"
    )
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
