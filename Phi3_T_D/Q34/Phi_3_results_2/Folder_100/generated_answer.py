def find_original_set(*sets):
    if not isinstance(sets, (list, set)) or not all((isinstance(s, set) for s in sets)):
        raise TypeError('All arguments must be sets of integers.')
    if len(sets) != 91:
        raise ValueError('Exactly 91 sets are required.')
    if len(set((frozenset(s) for s in sets))) != 91:
        raise ValueError('All sets must be distinct.')
    original_set = set()
    for s in sets:
        original_set.update(s)
    return original_set