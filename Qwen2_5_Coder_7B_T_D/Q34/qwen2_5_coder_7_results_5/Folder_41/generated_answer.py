from functools import reduce

def find_original_set(*sets):
    return reduce(lambda x, y: x.union(y), sets)