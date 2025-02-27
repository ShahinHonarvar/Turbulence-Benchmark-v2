def find_original_set(*args):
    if len(args) != 27:
        raise ValueError('Exactly 27 arguments are required')
    return set.intersection(*args)