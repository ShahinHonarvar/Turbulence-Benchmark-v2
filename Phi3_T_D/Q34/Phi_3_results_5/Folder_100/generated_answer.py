def find_original_set(*args):
    if len(args) != 91:
        raise ValueError('Exactly 91 arguments are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets.')
        original_set |= arg
    return original_set