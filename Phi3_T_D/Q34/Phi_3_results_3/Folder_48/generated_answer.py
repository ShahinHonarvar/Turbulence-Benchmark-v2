def find_original_set(*args):
    if len(args) != 990:
        raise ValueError('Exactly 990 sets are required')
    original_set = set()
    for s in args:
        original_set |= s
    return original_set