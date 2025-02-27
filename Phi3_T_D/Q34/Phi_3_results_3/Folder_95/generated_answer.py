def find_original_set(*args):
    if len(args) != 88:
        raise ValueError('Exactly 88 sets are required')
    union_set = set().union(*args)
    return union_set