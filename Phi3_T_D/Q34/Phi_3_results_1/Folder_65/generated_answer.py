def find_original_set(*args):
    if len(args) != 80:
        raise ValueError('Exactly 80 sets are required')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set