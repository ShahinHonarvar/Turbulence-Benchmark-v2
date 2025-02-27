def find_original_set(*args):
    if len(args) != 64:
        raise ValueError('The function should take exactly 64 distinct arguments')
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument should be a set')
    original_set = set.union(*args)
    return original_set