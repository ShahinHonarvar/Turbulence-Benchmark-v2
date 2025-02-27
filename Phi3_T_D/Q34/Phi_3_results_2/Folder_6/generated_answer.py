def find_original_set(*sets):
    if len(sets) != 276:
        raise ValueError('Exactly 276 sets are required.')
    all_elements = {element for s in sets for element in s}
    return all_elements