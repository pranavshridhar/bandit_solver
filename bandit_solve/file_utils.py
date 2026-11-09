"""
## `file_utils.py`
The container for the only two file utils I will ever need for this project
"""

def read_file(path: str) -> str:
    with open(path, 'r') as f:
        return f.read()

def write_file(path: str, contents: str) -> None:
    with open(path, 'w') as f:
        f.write(contents)

