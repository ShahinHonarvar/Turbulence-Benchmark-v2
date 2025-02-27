def find_original_set(*sets):
    if len(sets) != 19:
        raise ValueError('Exactly 19 sets are required')
    all_elements = set().union(*sets)
    return {element for element in all_elements if all((element in s for s in sets))}