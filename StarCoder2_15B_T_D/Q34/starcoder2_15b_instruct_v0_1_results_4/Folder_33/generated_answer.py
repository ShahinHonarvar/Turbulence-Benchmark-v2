def find_original_set(*args):
    if len(args) != 263:
        raise ValueError('Exactly 263 arguments are required.')
    smallest_set = set.intersection(*args)
    return smallest_set