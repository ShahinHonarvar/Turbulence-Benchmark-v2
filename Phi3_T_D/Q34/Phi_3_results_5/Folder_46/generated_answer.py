def find_original_set(*args):
    if len(args) != 828:
        raise ValueError('Exactly 828 sets are required as arguments')
    original_set = set().union(*args)
    return original_set