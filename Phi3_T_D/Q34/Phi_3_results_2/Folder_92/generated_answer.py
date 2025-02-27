def find_original_set(*args):
    if len(args) != 8:
        raise ValueError('Exactly 8 sets are required')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set