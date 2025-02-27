def find_original_set(*args):
    original_set = set()
    if len(args) != 48:
        raise ValueError('Exactly 48 arguments are required.')
    for arg in args:
        if len(arg) != len(set(arg)):
            raise ValueError('All arguments must contain distinct integers.')
        original_set |= arg
    return original_set