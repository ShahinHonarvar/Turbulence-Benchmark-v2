def find_original_set(*args):
    original_set = min(map(set.union, args))
    return original_set