def find_original_set(*args):
    original_set = set.union(*args)
    for arg in args:
        if not arg.issubset(original_set):
            raise ValueError('Each argument must be a subset of the original set')
    return original_set