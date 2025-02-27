def find_original_set(*args):
    if len(args) != 276:
        raise ValueError('Exactly 276 arguments are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        original_set.update(arg)
    return original_set