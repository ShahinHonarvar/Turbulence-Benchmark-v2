def find_original_set(*args):
    if len(args) != 126 or any((len(arg) != len(args[0]) for arg in args)):
        raise ValueError('Exactly 126 distinct arguments needed, each containing the same number of integers.')
    return set.union(*args)