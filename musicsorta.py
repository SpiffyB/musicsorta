import re
import argparse
import os
import pprint
import mutagen

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

def sort_by_regex(file):
    pattern = re.compile(r"(?P<artist>.+) - (?P<title>.+)\..+")
    
    match = re.match(pattern, file)
    if match is None:
        pass_list.append(file)
        return False
    else:
        if match.group("artist") not in dir_struct:
            dir_struct[match.group("artist")] = {}
        dir_struct[match.group("artist")][file] = match.group("title")
        return True
    

def validate_file(filename):
    if not filename.endswith(FILE_EXTENSIONS):
        pass_list.append(filename)
        return False
    return True

def main():
    args = parse_args()

    files = os.listdir(args.library)
    filtered_files = filter(validate_file, files)

    for song in filtered_files:
        sort_by_regex(song)

    pprint.pprint(dir_struct)
    pprint.pprint(pass_list)

if __name__ == "__main__":
    main()