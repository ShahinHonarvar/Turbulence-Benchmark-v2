def find_original_set(*args):
    if len(args) != 42:
        return None
    smallest_set = set()
    for arg in args:
        if not arg.issubset(smallest_set):
            return None
        smallest_set |= arg
    return smallest_set