def find_original_set(*args):
    if len(args) != 78:
        raise ValueError('The function must take exactly 78 distinct arguments')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument must be a set')
        original_set |= arg
    return original_set