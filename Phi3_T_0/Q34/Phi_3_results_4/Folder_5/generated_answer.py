def find_original_set(*args):
    if len(args) != 46:
        raise ValueError('Exactly 46 sets are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets')
        original_set.update(arg)
    return original_set