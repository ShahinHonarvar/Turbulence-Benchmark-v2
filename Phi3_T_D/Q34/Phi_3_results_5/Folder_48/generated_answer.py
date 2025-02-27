def find_original_set(*args):
    if len(args) != 990 or len(args) == 0:
        raise ValueError('Exactly 990 arguments are required as input')
    original_set = set().union(*args)
    return original_set