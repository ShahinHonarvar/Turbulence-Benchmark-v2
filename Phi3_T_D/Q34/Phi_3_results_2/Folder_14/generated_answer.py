def find_original_set(*args):
    if not args or any((len(s) != len(set(s)) for s in args)):
        raise ValueError('All arguments must be distinct sets of integers.')
    original_set = set().union(*args)
    return original_set