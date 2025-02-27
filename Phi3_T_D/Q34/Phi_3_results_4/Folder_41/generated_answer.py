def find_original_set(*args):
    if len(args) != 20:
        raise ValueError('Exactly 20 arguments are required.')
    original_set = set().union(*args)
    return original_set