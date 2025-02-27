def find_original_set(*sets):
    if len(sets) != 162:
        raise ValueError('Exactly 162 distinct sets are required.')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set