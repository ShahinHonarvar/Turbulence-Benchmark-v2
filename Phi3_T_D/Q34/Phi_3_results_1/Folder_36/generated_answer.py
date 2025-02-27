def find_original_set(*args):
    if len(args) > 714:
        raise ValueError('Too many arguments. Maximum of 714 sets are allowed.')
    union_set = set()
    for arg in args:
        union_set.update(arg)
    return union_set