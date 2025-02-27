def find_original_set(*sets):
    if len(sets) != 93:
        raise ValueError('Exactly 93 sets are required')
    original_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets of integers')
        for val in s:
            if not isinstance(val, int):
                raise TypeError('All elements in sets must be integers')
            original_set.add(val)
    return original_set