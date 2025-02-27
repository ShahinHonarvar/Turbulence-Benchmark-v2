def find_original_set(*args):
    if len(args) == 8:
        union_set = set().union(*args)
        return union_set
    else:
        raise ValueError('Exactly 8 distinct arguments required')