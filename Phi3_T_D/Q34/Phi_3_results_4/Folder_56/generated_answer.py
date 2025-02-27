def find_original_set(*others):
    if len(others) != 63:
        raise ValueError('Exactly 63 arguments are required, each being a set of integers.')
    original_set = others[0].copy()
    for s in others[1:]:
        original_set = original_set.union(s)
    return original_set