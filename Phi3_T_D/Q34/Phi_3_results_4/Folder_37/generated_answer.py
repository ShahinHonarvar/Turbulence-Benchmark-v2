def find_original_set(*args):
    if len(args) != 67:
        raise ValueError('Exactly 67 arguments are required')
    original_set = set().union(*args)
    return original_set