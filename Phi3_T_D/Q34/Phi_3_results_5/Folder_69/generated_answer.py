def find_original_set(*sets):
    if len(sets) != 126:
        raise ValueError('Exactly 126 sets are required')
    original_set = set().union(*sets)
    return original_set