def find_original_set(*args):
    if len(args) != 21:
        raise ValueError('The function requires exactly 21 distinct arguments.')
    original_set = set.union(*args)
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('Each argument must be a set of integers.')
    return original_set