def find_original_set(*args):
    if len(args) != 263:
        raise ValueError('Exactly 263 arguments required')
    union_set = set().union(*args)
    return union_set