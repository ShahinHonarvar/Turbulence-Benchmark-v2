def find_original_set(*sets):
    return reduce(lambda a, b: a.union(b), sets)