def find_original_set(*args):
    if len(args) != 41:
        raise ValueError('Exactly 41 arguments are required.')
    return set().union(*args)