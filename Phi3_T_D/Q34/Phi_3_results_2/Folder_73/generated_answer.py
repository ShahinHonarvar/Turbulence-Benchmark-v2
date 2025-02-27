def find_original_set(*args):
    if len(args) != 19:
        raise ValueError('Exactly 19 sets must be provided')
    original_set = set().union(*args)
    return original_set