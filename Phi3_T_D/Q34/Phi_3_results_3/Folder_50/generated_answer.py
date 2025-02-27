def find_original_set(*args):
    if len(args) != 99:
        raise ValueError('Exactly 99 arguments are required')
    union_set = set().union(*args)
    return union_set