def find_original_set(*sets):
    if len(sets) != 57:
        raise ValueError('Exactly 57 arguments are required, each being a set of integers.')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set