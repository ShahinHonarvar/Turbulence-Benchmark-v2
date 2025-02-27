def find_original_set(*sets):
    if len(sets) == 77:
        return set().union(*sets)
    else:
        return 'Error: Function requires exactly 77 sets as arguments.'