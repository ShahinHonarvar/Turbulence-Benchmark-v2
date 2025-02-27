def find_original_set(*sets):
    if len(sets) != 23:
        raise ValueError('Exactly 23 sets are required.')
    combined_set = set().union(*sets)
    unique_elements = {element for element in combined_set if all((element in s for s in sets))}
    return unique_elements