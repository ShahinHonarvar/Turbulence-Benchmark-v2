def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Exactly 990 arguments are required')
    original_set = set()
    for current_set in args:
        if not isinstance(current_set, set):
            raise TypeError('All arguments must be sets')
        original_set |= current_set
    return original_set