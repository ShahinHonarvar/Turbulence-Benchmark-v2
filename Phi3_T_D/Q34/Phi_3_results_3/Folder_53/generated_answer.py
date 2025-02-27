def find_original_set(*args):
    if len(args) == 84:
        original_set = set().union(*args)
        return original_set
    else:
        raise ValueError('Exactly 84 distinct arguments are required.')