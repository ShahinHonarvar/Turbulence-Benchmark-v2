def find_original_set(*args):
    if len(args) != 49:
        raise ValueError('Exactly 49 sets are required.')
    union_set = {}
    for arg in args:
        for element in arg:
            if element in union_set:
                continue
            union_set[element] = True
    return set(union_set.keys())