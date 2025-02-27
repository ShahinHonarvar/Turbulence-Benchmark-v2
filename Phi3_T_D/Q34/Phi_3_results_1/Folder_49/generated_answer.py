def find_original_set(*args):
    if len(args) != 60:
        raise ValueError('Exactly 60 arguments are required.')
    original_set = set().union(*args)
    return original_set