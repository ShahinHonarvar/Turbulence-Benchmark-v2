def find_original_set(*args):
    if len(args) != 73:
        raise ValueError('Expected exactly 73 arguments')
    original_set = set.union(*args)
    return original_set