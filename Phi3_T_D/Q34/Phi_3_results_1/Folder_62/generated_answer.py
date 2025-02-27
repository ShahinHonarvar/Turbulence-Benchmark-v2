def find_original_set(*args):
    if len(args) != 790:
        raise ValueError('Exactly 790 distinct sets are required.')
    union_set = set()
    for arg in args:
        union_set |= set(arg)
    return union_set