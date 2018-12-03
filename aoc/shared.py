import sys


def read_input_lines(path, convert_to=None):
    with open(path) as f:
        freqs = f.readlines()
    if convert_to:
        return [convert_to(f) for f in freqs]
    return [f.rstrip() for f in freqs]


def exec_cl_function():
    getattr(sys.modules['__main__'], sys.argv[1])()
