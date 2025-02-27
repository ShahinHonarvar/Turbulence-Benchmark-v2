def find_original_set(*args):
    if len(args) != 849:
        raise ValueError('Exactly 849 sets are required.')
    original_set = set().union(*args)
    return original_set