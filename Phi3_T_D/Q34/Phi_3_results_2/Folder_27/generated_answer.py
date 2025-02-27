def find_original_set(*args):
    if len(args) != 100 or any((len(set_) != len(set(set_)) for set_ in args)):
        raise ValueError('Input must be exactly 100 distinct sets of integers.')
    original_set = set().union(*args)
    return original_set