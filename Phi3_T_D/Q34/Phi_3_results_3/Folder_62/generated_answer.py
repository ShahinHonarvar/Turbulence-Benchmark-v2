def find_original_set(*args):
    if len(args) != 790:
        raise ValueError('Exactly 790 sets are required')
    return set().union(*args)