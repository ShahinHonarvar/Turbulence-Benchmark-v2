def find_original_set(*sets):
    if len(sets) != 73:
        raise ValueError('Exactly 73 sets are required.')
    original = set()
    for s in sets:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets.')
        if len(s) != len(set(s)):
            raise ValueError('Duplicate values in set are not allowed.')
        original.update(s)
    return original