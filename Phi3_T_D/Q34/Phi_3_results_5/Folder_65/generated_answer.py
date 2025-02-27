def find_original_set(sets):
    if len(sets) != 80:
        raise ValueError('Exactly 80 sets are required.')
    original_set = set().union(*sets)
    return original_set