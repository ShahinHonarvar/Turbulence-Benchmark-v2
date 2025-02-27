def find_original_set(*sets):
    if len(sets) != 985:
        raise ValueError('Exactly 985 sets are required')
    original_set = set()
    for s in sets:
        if not isinstance(s, set):
            raise ValueError(f'All arguments must be sets, got {type(s)} instead')
        original_set.update(s)
    return set(sorted(original_set))