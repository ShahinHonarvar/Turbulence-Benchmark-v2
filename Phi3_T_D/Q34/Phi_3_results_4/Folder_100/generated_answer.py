def find_original_set(*args):
    if len(args) != 91:
        raise ValueError('Exactly 91 distinct sets are required as arguments')
    original_set = set().union(*args)
    return original_set