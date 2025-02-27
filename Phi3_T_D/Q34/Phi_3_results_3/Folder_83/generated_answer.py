def find_original_set(*args):
    if len(args) != 64:
        raise ValueError('Exactly 64 sets are required.')
    original_set = set().union(*args)
    return original_set