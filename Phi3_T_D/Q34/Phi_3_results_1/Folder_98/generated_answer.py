def find_original_set(*sets):
    if len(sets) != 9:
        raise ValueError('Exactly 9 distinct sets are required.')
    union_set = set.union(*sets)
    return union_set