def find_original_set(*args):
    if len(args) != 46:
        raise ValueError('Exactly 46 arguments are required.')
    original_set = set().union(*args)
    return original_set