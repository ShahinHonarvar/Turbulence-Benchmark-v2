def find_original_set(*args):
    if len(args) != 42:
        raise ValueError('Exactly 42 sets are required.')
    original_set = set().union(*args)
    return original_set