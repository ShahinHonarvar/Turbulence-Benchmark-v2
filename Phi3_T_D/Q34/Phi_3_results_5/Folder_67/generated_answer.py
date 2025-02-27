def find_original_set(*sets):
    if len(sets) != 42:
        raise ValueError('Exactly 42 sets are required')
    original_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise TypeError('Each argument must be a set')
        original_set.update(s)
    return original_set