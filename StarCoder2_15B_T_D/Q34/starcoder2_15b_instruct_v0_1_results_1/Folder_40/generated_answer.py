def find_original_set(*args):
    if len(args) < 1:
        raise ValueError('The function should take at least 1 argument.')
    smallest_set = set()
    for arg in args:
        smallest_set = smallest_set.union(arg)
    return smallest_set