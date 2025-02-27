def find_original_set(*args):
    if len(args) != 49:
        raise ValueError('Exactly 49 distinct arguments are required.')
    return set().union(*args)