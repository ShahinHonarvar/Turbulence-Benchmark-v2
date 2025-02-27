def find_original_set(*args):
    if len(args) == 85:
        return set().union(*args)
    else:
        raise ValueError('Exactly 85 arguments are required')