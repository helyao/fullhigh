import sys

def print_error(*obj):
    print("Error:", *obj, file=sys.stderr)