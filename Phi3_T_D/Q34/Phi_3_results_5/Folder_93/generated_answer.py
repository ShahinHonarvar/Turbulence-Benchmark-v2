def find_original_set(*args):
    if len(args) != 90:
        raise ValueError('Exactly 90 distinct arguments are required.')
    union_set = set().union(*args)
    return union_set