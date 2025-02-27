def find_original_set(*args):
    if len(args) != 410:
        raise ValueError('Exactly 410 arguments are required')
    union_set = set().union(*args)
    return union_set