def find_original_set(*args):
    if len(args) != 37:
        raise ValueError('Exactly 37 sets are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets of integers')
        original_set |= arg
    return original_set