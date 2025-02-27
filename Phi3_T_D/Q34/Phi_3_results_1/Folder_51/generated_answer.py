def find_original_set(*args):
    if len(args) != 28:
        raise ValueError('Exactly 28 sets are required')
    union_set = set().union(*args)
    return union_set