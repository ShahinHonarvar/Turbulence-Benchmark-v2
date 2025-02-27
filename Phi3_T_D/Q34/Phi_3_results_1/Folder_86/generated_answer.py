def find_original_set(*sets):
    if len(sets) != 162:
        raise ValueError('Exactly 162 sets are required.')
    original_set = set().union(*sets)
    return original_set