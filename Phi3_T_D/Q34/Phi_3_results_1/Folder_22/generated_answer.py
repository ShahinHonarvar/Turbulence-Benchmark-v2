def find_original_set(*sets):
    if len(sets) != 24:
        raise ValueError('Exactly 24 arguments are required')
    union_set = set().union(*sets)
    return union_set