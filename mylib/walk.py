# create a function that recursively walks a directory tree and returns files that match a pattern
# use pathlib

import pathlib
import re


def walk(
    path="/workspaces/assimilate-python-from-zero/assets",
    pattern=None,
    ignore=".hidden",
):
    """Walk a directory tree and return files that match a pattern
    Also ignore patterns in a full path
    """
    if pattern == None:
        print("searching for audio and video files")
        pattern = r".*\.(mp4|mov|mkv|avi|mp3|wav|flac|ogg)$"
    path = pathlib.Path(path)
    for p in path.rglob("*"):
        if p.is_file() and re.match(pattern, p.name) and not re.search(ignore, str(p)):
            yield p


if __name__ == "__main__":
    for p in walk():
        print(p)
