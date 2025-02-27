def find_original_set(*sets):
    if len(sets) != 4:
        raise ValueError('Exactly 4 distinct sets are required')
    original_set = set().union(*sets)
    return original_set