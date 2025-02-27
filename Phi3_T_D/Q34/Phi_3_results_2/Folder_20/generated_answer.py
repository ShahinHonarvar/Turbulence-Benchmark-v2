def find_original_set(*sets):
    if len(sets) != 66:
        raise ValueError('Exactly 66 sets are required.')
    return set.union(*sets)