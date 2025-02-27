def find_original_set(*args):
    if len(args) != 20 or any((len(arg) != len(set(arg)) for arg in args)):
        raise ValueError('Each argument must be a set of distinct integers')
    original_set = set()
    for subset in args:
        original_set.update(subset)
    return original_set