def find_original_set(*args):
    if len(args) != 5:
        raise ValueError('Exactly 5 arguments are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument must be a set.')
        original_set |= arg
    return original_set