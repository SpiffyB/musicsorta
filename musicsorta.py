import re
import argparse
import os

dir_struct = {}

def parse_args():
    parser = argparse.ArgumentParser(description='Music library sorter')
    parser.add_argument(
        'library',
        help="Location of music library"
    )
    return parser.parse_args()


def main():
    pattern = re.compile(r"(.+) - (.+)\..+")
    args = parse_args()

    for filename in os.listdir(args.library):
        match = re.match(pattern, filename)
        if match.group(1) not in dir_struct:
            dir_struct[match.group(1)] = {}
        dir_struct[match.group(1)][match.group(2)] = filename

if __name__ == "__main__":
    main()