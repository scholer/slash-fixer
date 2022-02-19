

import argparse
from pathlib import Path


def fix_slashes_cli():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('path')

    args = argparser.parse_args()

    path_str = args.path
    path = Path(path_str)

    if "/" in path_str:
        print(path_str.replace('/', '\\'), end="")
    else:
        print(path_str.replace('\\', '/'), end="")

if __name__ == "__main__":
    fix_slashes_cli()
