def find_original_set(*sets):
    if len(sets) != 99 or not all(map(lambda x: isinstance(x, set), sets)):
        raise ValueError('Function requires exactly 99 sets of integers.')
    original_set = set().union(*sets)
    return original_set