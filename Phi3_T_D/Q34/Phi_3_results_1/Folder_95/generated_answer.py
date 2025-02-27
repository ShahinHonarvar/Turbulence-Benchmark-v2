def find_original_set(*sets):
    if len(sets) != 88:
        raise ValueError('Exactly 88 sets are required')
    original_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise TypeError("All arguments must be of type 'set'")
        original_set.update(s)
    return original_set