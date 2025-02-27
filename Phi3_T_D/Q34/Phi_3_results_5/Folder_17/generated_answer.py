def find_original_set(*args):
    if len(args) != 478:
        raise ValueError('Exactly 478 sets are required.')
    original_set = set().union(*args)
    return original_set