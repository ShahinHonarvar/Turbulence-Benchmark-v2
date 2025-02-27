def find_original_set(*args):
    if len(args) != 85:
        raise ValueError('Exactly 85 arguments are needed')
    return set().union(*args)