def find_original_set(*args):
    if len(args) != 194:
        raise ValueError('Exactly 194 set arguments are required')
    original_set = set().union(*args)
    return original_set