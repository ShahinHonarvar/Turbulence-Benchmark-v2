def find_original_set(*sets):
    if len(sets) != 87:
        raise ValueError('Exactly 87 sets are required')
    original_set = set()
    for s in sets:
        original_set |= s
    return original_set