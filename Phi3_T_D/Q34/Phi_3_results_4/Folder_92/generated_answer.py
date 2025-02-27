def find_original_set(*args):
    if len(args) != 8 or any((len(arg) != len(set(arg)) for arg in args)):
        raise ValueError('Arguments must be 8 distinct sets of integers with no duplicates.')
    return set().union(*args)