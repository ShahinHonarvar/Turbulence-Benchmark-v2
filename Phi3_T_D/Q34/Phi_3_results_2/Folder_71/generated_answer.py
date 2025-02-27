def find_original_set(*args):
    if len(args) != 16:
        raise ValueError('Exactly 16 arguments are required.')
    if len(set(map(len, args))) != 1:
        raise ValueError('All sets must be of the same size.')
    union_set = set().union(*args)
    return sorted(list(union_set))