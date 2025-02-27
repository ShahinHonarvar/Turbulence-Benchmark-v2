def find_original_set(*args):
    if not args or len(args) != 28:
        raise ValueError('Exactly 28 distinct sets are required.')
    original_set = set()
    for arg_set in args:
        original_set.update(arg_set)
    return original_set