def find_original_set(*sets):
    if len(sets) != 100:
        raise ValueError('Exactly 100 sets are required')
    original_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise ValueError('All arguments must be sets')
        original_set.update(s)
    return original_set