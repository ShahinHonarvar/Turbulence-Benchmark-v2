def find_original_set(*args):
    if len(args) != 49:
        raise ValueError('Function requires exactly 49 sets')
    original_set = set()
    for s in args:
        if not isinstance(s, set):
            raise ValueError('All arguments must be sets')
        original_set |= s
    return original_set