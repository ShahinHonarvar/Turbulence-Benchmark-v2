def find_original_set(*args):
    if len(args) != 276:
        raise ValueError('Exactly 276 sets are required')
    union_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument must be a set of integers')
        union_set |= arg
    return union_set