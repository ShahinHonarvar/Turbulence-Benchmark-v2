def find_original_set(*sets):
    return min(sets, key=lambda s: len(s.union(*sets)))