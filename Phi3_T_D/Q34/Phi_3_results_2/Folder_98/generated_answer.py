def find_original_set(*sets):
    if len(sets) != 9:
        raise ValueError('Exactly 9 distinct sets are required.')
    original_set = set().union(*sets)
    return original_set