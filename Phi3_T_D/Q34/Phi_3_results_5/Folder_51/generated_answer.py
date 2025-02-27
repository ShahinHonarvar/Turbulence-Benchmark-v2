def find_original_set(*sets):
    if len(sets) != 28:
        raise ValueError('Exactly 28 distinct sets are required')
    original_set = set().union(*sets)
    return original_set