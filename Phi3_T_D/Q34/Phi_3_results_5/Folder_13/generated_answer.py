def find_original_set(*args):
    if len(args) != 845:
        raise ValueError('Exactly 845 sets are required as arguments.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets.')
        original_set.update(arg)
    return original_set