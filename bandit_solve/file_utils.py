"""
## `file_utils.py`
The container for the only two file utils I will ever need for this project
"""

import os

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()

def write_file(path: str, contents: str) -> None:
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    fd = os.open(path = path, flags = os.O_WRONLY | os.O_CREAT | os.O_TRUNC, mode=0o600)
    with open(fd, 'w') as f:
        f.write(contents)

