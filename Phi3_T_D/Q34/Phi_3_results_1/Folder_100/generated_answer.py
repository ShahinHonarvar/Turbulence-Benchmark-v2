def find_original_set(*args):
    if len(args) != 91:
        raise ValueError('Exactly 91 sets are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be of type set.')
        original_set |= arg
    return original_set