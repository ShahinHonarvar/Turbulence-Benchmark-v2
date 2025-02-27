def find_original_set(*args):
    if len(args) != 90:
        raise ValueError('Exactly 90 arguments are required')
    union_set = set()
    for arg in args:
        union_set |= arg
    return union_set