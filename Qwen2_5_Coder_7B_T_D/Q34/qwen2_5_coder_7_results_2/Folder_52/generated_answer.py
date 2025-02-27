def find_original_set(*sets):
    original_set = set()
    for arg in sets:
        original_set.update(arg)
    return original_set