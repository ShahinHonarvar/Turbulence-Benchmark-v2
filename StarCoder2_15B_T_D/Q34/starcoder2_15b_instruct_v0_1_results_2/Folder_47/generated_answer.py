def find_original_set(*args):
    if len(args) != 77:
        raise ValueError('Expected exactly 77 arguments')
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Expected a set of integers as an argument')
    original_set = set()
    for arg in args:
        original_set |= arg
    return original_set