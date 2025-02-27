def find_original_set(*args):
    if len(args) != 88:
        raise ValueError('Invalid number of arguments. Expected 88, got {}'.format(len(args)))
    original_set = set.union(*args)
    for arg in args:
        if not set(arg).issubset(original_set):
            raise ValueError('Invalid argument. {} is not a subset of the original set'.format(arg))
    return original_set