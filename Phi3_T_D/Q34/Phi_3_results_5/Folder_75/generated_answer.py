def find_original_set(*args):
    if len(args) != 15:
        raise ValueError('Exactly 15 sets are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        original_set |= arg
    return set(original_set)