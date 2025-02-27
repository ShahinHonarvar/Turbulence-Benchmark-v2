def find_original_set(*sets):
    if len(sets) != 66:
        raise ValueError('The function must take exactly 66 sets.')
    original_set = set()
    for set_ in sets:
        original_set.update(set_)
    return original_set