def find_original_set(*sets):
    if not isinstance(sets, tuple) or len(sets) != 7 or len(set(map(len, sets))) != 1:
        raise ValueError('Input should be exactly 7 distinct sets of integers.')
    original_set = set().union(*sets)
    return original_set