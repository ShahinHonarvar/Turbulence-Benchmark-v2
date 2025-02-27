def find_original_set(*args):
    if len(args) != 56:
        raise ValueError('Exactly 56 distinct arguments are required')
    base_set = set()
    for arg in args:
        base_set |= arg
    return base_set