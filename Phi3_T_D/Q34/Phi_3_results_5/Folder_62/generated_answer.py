def find_original_set(*args):
    if len(args) > 790:
        raise ValueError('Too many arguments provided')
    original_set = set()
    for subset in args:
        original_set.update(subset)
    return original_set