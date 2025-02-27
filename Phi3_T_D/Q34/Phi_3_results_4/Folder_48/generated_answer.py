def find_original_set(*sets):
    if len(sets) != 990 or any((len(s) != len(sets[0]) for s in sets)):
        raise ValueError('Exactly 990 sets of integers of equal size are required.')
    return set.union(*sets)