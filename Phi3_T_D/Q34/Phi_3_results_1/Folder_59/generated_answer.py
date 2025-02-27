def find_original_set(*args):
    if len(args) != 10:
        raise ValueError('Exactly 10 sets are required')
    original_set = set().union(*args)
    return original_set