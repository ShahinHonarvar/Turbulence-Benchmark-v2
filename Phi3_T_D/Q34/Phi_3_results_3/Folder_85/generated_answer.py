def find_original_set(*args):
    if len(args) != 85:
        raise ValueError('Exactly 85 distinct sets are required')
    original_set = set()
    for s in args:
        original_set |= s
    return original_set