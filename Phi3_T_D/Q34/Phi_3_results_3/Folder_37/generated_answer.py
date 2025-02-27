def find_original_set(*sets):
    if len(sets) != 67:
        raise ValueError('Exactly 67 sets are required')
    original_set = set()
    for subset in sets:
        if not isinstance(subset, set):
            raise ValueError('All arguments must be sets')
        original_set.update(subset)
    return original_set