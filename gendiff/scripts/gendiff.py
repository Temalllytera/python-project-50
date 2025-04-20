import argparse
import json

def parse_file(file_path):
    with open(file_path) as f:
        parsed = json.load(f)
        return parsed


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    print(f"Comparing {args.first_file} and {args.second_file}")
    first_parsed = parse_file(args.first_file)
    print(first_parsed)

if __name__ == '__main__':
    main()
    