def find_original_set(*args):
    if not args or len(args) != 7:
        raise ValueError('Exactly 7 distinct sets are required.')
    union_set = set().union(*args)
    return union_set