def find_original_set(*sets):
    if len(sets) != 18 or any((len(s) != len(sets[0]) for s in sets)):
        raise ValueError('Exactly 18 distinct sets of equal length are required.')
    original_set = set().union(*sets)
    return original_set