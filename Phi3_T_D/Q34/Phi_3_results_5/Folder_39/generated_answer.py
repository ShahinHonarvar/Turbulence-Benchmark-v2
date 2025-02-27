def find_original_set(*args):
    if len(args) != 21:
        raise ValueError('Exactly 21 arguments are required.')
    union_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        union_set |= arg
    return union_set