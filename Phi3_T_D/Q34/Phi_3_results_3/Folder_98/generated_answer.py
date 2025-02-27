def find_original_set(*sets):
    if len(sets) != 9 or any((len(s) != len(sets[0]) for s in sets)):
        raise ValueError('Exactly 9 distinct sets with equal length are required.')
    return set.union(*sets)