def find_original_set(*args):
    if len(args) != 415:
        raise ValueError('Exactly 415 arguments are expected')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets of integers')
        original_set.update(arg)
    return original_set