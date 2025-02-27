def find_original_set(*args):
    if len(args) != 92:
        raise ValueError('Exactly 92 arguments are expected')
    original_set = set().union(*args)
    return original_set