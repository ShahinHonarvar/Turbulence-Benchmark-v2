def find_original_set(*sets):
    if len(sets) != 453 or any((len(s) != len(sets[0]) for s in sets[1:])):
        raise ValueError('Exactly 453 distinct arguments are required, all of equal size.')
    original_set = sets[0].copy()
    for s in sets[1:]:
        original_set.update(s)
    return original_set