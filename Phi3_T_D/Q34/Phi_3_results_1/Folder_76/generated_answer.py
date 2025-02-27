def find_original_set(a1, a2, a3, *args):
    original_set = set(a1)
    for arg in (a2, a3) + args:
        original_set.update(arg)
    return original_set