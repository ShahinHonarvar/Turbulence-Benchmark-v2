def find_original_set(*args):
    if len(args) != 263:
        raise ValueError('Exactly 263 arguments are required')
    original_set = set().union(*args)
    return original_set