def find_original_set(*args):
    if len(args) != 459:
        raise ValueError('Exactly 459 sets are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets of integers')
        original_set.update(arg)
    return original_set