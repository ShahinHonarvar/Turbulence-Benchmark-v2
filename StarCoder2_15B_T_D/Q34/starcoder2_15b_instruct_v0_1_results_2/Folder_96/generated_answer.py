def find_original_set(*args):
    original_set = set.union(*args)
    for arg in args:
        if len(arg) != len(original_set):
            raise ValueError('All arguments must be distinct sets')
    return original_set