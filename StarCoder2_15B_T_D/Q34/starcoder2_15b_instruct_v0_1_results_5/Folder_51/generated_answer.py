def find_original_set(*args):
    distinct_args = list(set(args))
    smallest_set = set()
    for arg in distinct_args:
        smallest_set |= arg
    return smallest_set