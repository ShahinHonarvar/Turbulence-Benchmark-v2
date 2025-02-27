def find_original_set(*args):
    if len(args) != 926:
        raise ValueError('Exactly 926 sets are required.')
    return set.union(*args)