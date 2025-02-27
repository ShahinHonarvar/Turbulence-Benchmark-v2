def find_original_set(*args):
    if len(args) != 84:
        raise ValueError('Exactly 84 sets are required as arguments.')
    original_set = set()
    for arg_set in args:
        original_set.update(arg_set)
    return set(sorted(original_set))