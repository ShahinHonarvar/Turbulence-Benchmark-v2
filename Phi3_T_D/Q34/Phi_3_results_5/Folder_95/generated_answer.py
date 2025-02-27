def find_original_set(*args):
    if len(args) != 88:
        raise ValueError('Exactly 88 arguments required')
    original_set = set().union(*args)
    return original_set