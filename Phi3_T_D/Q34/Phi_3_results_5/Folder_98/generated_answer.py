def find_original_set(*sets):
    if len(sets) != 9 or len(set(map(len, sets))) != 1:
        raise ValueError('Exactly 9 distinct sets are required.')
    original_set = set().union(*sets)
    return original_set