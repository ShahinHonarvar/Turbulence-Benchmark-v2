def find_original_set(*args):
    if len(args) != 77:
        raise ValueError('Exactly 77 arguments are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('Argument must be a set')
        original_set.update(arg)
    return original_set