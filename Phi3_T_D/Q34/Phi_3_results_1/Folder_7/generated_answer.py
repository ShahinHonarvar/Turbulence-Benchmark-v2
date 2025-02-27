def find_original_set(*args):
    if len(args) != 537:
        raise ValueError('Exactly 537 sets are required')
    original_set = set().union(*args)
    return original_set