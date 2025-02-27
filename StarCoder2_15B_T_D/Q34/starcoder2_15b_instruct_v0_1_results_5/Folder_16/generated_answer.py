def find_original_set(*args):
    smallest_set = set()
    for arg in args:
        if not arg.issubset(smallest_set):
            smallest_set |= arg
    return smallest_set