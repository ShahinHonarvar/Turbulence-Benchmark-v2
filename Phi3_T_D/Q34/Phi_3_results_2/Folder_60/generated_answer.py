def find_original_set(*sets):
    return_set = set()
    for subset in sets:
        return_set.update(subset)
    return return_set