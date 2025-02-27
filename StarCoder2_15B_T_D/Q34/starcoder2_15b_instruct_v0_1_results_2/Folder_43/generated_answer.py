def find_original_set(*args):
    if len(args) != 49:
        raise ValueError('The function must be called with exactly 49 arguments.')
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument must be a set of integers.')
    original_set = set.union(*args)
    return original_set