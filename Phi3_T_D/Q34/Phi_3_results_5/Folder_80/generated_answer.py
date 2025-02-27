def find_original_set(*args):
    if len(args) > 453:
        raise ValueError('Too many arguments. Expecting exactly 453.')
    original_set = set().union(*args)
    return original_set