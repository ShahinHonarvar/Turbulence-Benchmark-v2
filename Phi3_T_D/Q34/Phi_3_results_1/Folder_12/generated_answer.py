def find_original_set(*args):
    if len(args) != 51:
        raise ValueError('Exactly 51 distinct arguments required, each a set of integers')
    return set().union(*args)