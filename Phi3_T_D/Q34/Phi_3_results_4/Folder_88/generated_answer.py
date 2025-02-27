def find_original_set(*sets):
    if len(sets) != 27:
        raise ValueError('Exactly 27 sets are required.')
    original_set = set().union(*sets)
    return original_set