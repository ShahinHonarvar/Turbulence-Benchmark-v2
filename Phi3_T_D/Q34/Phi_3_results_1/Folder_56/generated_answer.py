def find_original_set(*args):
    if len(args) != 63:
        raise ValueError('Exactly 63 arguments are required.')
    original_set = set.union(*args)
    return original_set