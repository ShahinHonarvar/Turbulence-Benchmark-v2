def find_original_set(*args):
    if len(args) != 459:
        raise ValueError('Exactly 459 arguments are required.')
    return set.union(*args)