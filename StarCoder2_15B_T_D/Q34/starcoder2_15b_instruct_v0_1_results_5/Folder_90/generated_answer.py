def find_original_set(*args):
    smallest_set = set()
    for arg in args:
        smallest_set.update(arg)
    for arg in args:
        if not arg.issubset(smallest_set):
            raise ValueError('Not all arguments are subsets of the smallest set')
    return smallest_set