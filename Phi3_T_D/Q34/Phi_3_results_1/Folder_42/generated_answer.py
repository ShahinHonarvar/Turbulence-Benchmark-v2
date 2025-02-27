def find_original_set(*sets):
    if len(sets) != 849:
        raise ValueError('Exactly 849 sets are required.')
    original_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets.')
        original_set |= s
    return original_set