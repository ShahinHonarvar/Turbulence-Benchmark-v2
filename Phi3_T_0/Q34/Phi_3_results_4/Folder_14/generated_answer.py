def find_original_set(*args):
    if len(args) != 13:
        raise ValueError('Exactly 13 arguments are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets')
        original_set.update(arg)
    return original_set