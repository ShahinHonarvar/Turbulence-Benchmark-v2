def find_original_set(*args):
    united_set = set()
    for s in args:
        united_set.update(s)
    original_set = set(united_set)
    return original_set