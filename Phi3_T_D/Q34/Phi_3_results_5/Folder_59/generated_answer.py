def find_original_set(*sets):
    if len(sets) != 10:
        raise ValueError('Exactly 10 arguments are required')
    original_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets')
        original_set |= s
    return original_set