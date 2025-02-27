def find_original_set(*sets):
    if len(sets) != 63:
        raise ValueError('Exactly 63 arguments are required.')
    original_set = set().union(*sets)
    return original_set