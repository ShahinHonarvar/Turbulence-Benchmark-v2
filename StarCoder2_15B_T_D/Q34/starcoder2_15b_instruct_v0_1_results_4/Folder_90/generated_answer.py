def find_original_set(*args):
    return min((set.union(*args) for set in args))