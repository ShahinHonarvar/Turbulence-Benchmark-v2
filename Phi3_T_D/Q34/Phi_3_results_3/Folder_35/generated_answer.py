def find_original_set(*args):
    original_set = set()
    if len(args) != 702:
        raise ValueError('Exactly 702 arguments are required')
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets of integers')
        original_set.update(arg)
    return original_set