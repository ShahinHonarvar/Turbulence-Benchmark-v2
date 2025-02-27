def find_original_set(*args):
    original_set = set()
    for arg in args:
        original_set.update(arg)
    original_set = sorted(list(original_set))
    return set(original_set)