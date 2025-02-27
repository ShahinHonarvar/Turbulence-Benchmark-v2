def find_original_set(*args):
    if len(args) != 97:
        raise ValueError('Exactly 97 arguments are required')
    original_set = set().union(*args)
    return original_set