def find_original_set(*args):
    if len(args) != 59:
        raise ValueError('Exactly 59 arguments are required')
    union_set = set().union(*args)
    return union_set