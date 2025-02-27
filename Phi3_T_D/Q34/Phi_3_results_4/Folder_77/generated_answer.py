def find_original_set(*args):
    if len(args) != 410:
        raise ValueError('Exactly 410 distinct sets are required')
    union_set = set()
    for arg in args:
        union_set.update(arg)
    return union_set