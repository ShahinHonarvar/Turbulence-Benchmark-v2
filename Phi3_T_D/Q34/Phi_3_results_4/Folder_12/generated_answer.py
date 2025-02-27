def find_original_set(*sets):
    if not isinstance(sets, (list, tuple)) or len(sets) != 51:
        raise ValueError('Exactly 51 arguments are required.')
    original_set = set()
    prev = set()
    for s in sets:
        if not (isinstance(s, set) and len(s) == len(set(s))):
            raise ValueError('Each argument must be a set of integers.')
        original_set.update(s)
        if prev != prev.union(s):
            return None
        prev = original_set.copy()
    return original_set