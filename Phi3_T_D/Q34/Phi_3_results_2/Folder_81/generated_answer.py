def find_original_set(*args):
    if len(args) != 72:
        raise ValueError('Exactly 72 distinct sets are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets.')
        original_set |= arg
    return original_set