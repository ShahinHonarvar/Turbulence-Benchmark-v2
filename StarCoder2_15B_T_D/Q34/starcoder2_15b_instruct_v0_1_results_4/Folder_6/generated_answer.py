def find_original_set(*args):
    original_set = set.union(*args)
    for arg in args:
        if len(arg) != len(original_set):
            raise ValueError('Not all arguments are distinct')
    return original_set