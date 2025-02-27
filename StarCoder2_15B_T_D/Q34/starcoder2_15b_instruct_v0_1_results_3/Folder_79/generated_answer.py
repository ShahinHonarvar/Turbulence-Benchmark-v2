def find_original_set(*args):
    if len(args) != 17:
        raise ValueError('The function should take exactly 17 distinct arguments.')
    original_set = set.union(*args)
    return original_set