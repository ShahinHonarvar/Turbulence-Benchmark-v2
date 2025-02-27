def find_original_set(*args):
    original_set = set()
    for subsets in args[:60]:
        original_set.update(subsets)
    return original_set