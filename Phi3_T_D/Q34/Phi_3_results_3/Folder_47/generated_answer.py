def find_original_set(*sets):
    if len(sets) != 77:
        raise ValueError('Exactly 77 sets are required')
    return set.intersection(*sets) if all(sets) else set()