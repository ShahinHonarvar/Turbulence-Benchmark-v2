def find_original_set(sets):
    if not sets:
        return set()
    original_set = set.union(*sets)
    return original_set