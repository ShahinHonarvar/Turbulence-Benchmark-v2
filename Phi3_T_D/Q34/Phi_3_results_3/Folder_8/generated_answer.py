def find_original_set(*sets):
    if len(sets) > 45:
        raise ValueError('Too many arguments. Must be exactly 45 sets.')
    result_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets.')
        result_set.update(s)
    return result_set