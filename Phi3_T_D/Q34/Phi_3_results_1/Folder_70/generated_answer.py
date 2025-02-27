def find_original_set(*args):
    if len(args) != 312:
        raise ValueError('Exactly 312 arguments are required, each is a set of integers.')
    original_set = set().union(*args)
    return original_set