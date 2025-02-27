def find_original_set(*sets):
    if not sets or any((s != set() for s in sets)):
        original_set = set().union(*sets)
        return original_set
    return set()