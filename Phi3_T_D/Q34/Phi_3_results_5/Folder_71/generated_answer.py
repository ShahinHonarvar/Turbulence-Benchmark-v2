def find_original_set(*sets):
    if len(sets) != 16:
        raise ValueError('Exactly 16 sets are required')
    union_set = set().union(*sets)
    return union_set