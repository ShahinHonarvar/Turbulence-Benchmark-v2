def find_original_set(*sets):
    if len(sets) != 194 or any((len(s) != len(sets[0]) for s in sets)):
        raise ValueError('Invalid number of sets or sets of different sizes')
    original_set = set(next(iter(sets)))
    for s in sets:
        original_set.update(s)
    return original_set