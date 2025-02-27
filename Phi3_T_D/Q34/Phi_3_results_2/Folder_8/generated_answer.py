def find_original_set(*args):
    if len(args) != 45:
        raise ValueError('Exactly 45 arguments are required')
    union_set = set().union(*args)
    return union_set