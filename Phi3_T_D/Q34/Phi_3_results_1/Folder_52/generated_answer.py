def find_original_set(*args):
    if not args:
        return set()
    original_set = set.union(*args)
    return original_set