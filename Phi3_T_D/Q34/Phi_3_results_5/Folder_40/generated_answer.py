def find_original_set(sets):
    if not sets:
        return set()
    result_set = sets[0]
    for current_set in sets[1:]:
        result_set |= current_set
    return result_set