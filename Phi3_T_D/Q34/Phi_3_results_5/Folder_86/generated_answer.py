def find_original_set(*args):
    if len(args) != 162 or len(set(map(len, args))) != 1:
        raise ValueError('Exactly 162 distinct arguments are required')
    original_set = set()
    for arg_set in args:
        original_set.update(arg_set)
    return original_set