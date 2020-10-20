import re
import argparse
import os
import pprint

FILE_EXTENSIONS = (".mp3", ".wav", ".m4a", ".flac")

dir_struct = {}
pass_list = []

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
        if not filename.endswith(FILE_EXTENSIONS):
            continue

        match = re.match(pattern, filename)
        if match is None:
            pass_list.append(filename)
        else:
            if match.group(1) not in dir_struct:
                dir_struct[match.group(1)] = {}
            dir_struct[match.group(1)][match.group(2)] = filename

if __name__ == "__main__":
    main()