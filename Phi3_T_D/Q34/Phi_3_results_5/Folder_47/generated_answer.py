def find_original_set(*args):
    if len(args) != 77:
        raise ValueError('Exactly 77 arguments are required')
    original_set = set()
    for s in args:
        if not isinstance(s, set):
            raise ValueError('Each argument must be a set of integers')
        original_set.update(s)
    return original_set