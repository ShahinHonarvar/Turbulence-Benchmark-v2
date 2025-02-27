def find_original_set(*args):
    smallest_set = set.union(*args)
    for arg in args:
        if arg <= smallest_set:
            continue
        else:
            raise ValueError('Not all arguments are subsets of the smallest set.')
    return smallest_set