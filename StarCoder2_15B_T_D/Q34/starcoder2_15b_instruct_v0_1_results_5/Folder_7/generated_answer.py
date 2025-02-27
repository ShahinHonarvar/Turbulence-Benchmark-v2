def find_original_set(*args):
    smallest_set = set()
    for s in args:
        smallest_set.update(s)
    return smallest_set