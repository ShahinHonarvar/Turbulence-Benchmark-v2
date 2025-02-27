def find_original_set(*args):
    if len(args) != 162:
        raise ValueError('Exactly 162 arguments are required')
    original_set = set()
    for arg_set in args:
        if not isinstance(arg_set, set):
            raise TypeError('All arguments must be sets of integers')
        original_set.update(arg_set)
    return original_set