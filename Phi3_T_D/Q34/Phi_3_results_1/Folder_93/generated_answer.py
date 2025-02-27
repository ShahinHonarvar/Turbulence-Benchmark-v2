def find_original_set(*sets):
    if len(sets) != 90:
        raise ValueError('Exactly 90 arguments are required.')
    original_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets.')
        if len(s) != len(set(s)):
            raise ValueError('All sets must contain distinct elements.')
        original_set.update(s)
    return original_set