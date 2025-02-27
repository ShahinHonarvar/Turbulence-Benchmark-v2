def find_original_set(*args):
    if not args or len(args) != 321:
        raise ValueError('Exactly 321 distinct arguments are required, each being a set of integers.')
    original_set = set().union(*args)
    return original_set