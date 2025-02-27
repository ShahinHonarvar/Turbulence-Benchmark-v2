def find_original_set(*sets):
    if len(sets) != 132:
        raise ValueError('Exactly 132 sets are required.')
    return set().union(*sets)