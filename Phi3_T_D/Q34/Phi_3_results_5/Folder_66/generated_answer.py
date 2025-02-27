def find_original_set(*sets):
    if len(sets) != 25:
        raise ValueError('Exactly 25 sets are required')
    superset = set.union(*sets)
    return superset