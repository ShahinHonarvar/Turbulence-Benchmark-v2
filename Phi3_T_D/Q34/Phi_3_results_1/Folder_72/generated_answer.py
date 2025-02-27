def find_original_set(*args):
    if len(args) != 87:
        raise ValueError('Exactly 87 distinct arguments are required')
    original_set = set.union(*args)
    return original_set