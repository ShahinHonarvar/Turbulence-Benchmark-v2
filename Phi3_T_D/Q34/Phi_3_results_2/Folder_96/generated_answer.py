def find_original_set(*args):
    if len(args) == 68:
        union_set = set().union(*args)
        return union_set
    else:
        raise ValueError('Exactly 68 sets required')