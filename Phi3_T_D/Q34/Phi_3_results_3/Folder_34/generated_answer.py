def find_original_set(*sets):
    if len(sets) != 95:
        raise ValueError('Exactly 95 distinct arguments are required')
    original_set = set().union(*sets)
    return original_set