def find_original_set(*args):
    original_set = set.union(*args)
    for arg in args:
        if len(arg) != len(set(arg)):
            raise ValueError('All arguments must be sets of distinct integers')
    return original_set