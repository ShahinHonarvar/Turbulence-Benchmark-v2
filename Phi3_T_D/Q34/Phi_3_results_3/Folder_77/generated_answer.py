def find_original_set(*sets):
    if len(sets) != 410:
        raise ValueError('Exactly 410 sets are required.')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set