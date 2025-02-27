def find_original_set(*args):
    if len(args) != 10:
        raise ValueError('Exactly 10 arguments required, each a set of integers.')
    union_set = set()
    for s in args:
        union_set |= s
    return sorted(union_set)