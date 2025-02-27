def find_original_set(*sets):
    if len(sets) != 845:
        raise ValueError('Exactly 845 sets are required.')
    original_set = set()
    for s in sets:
        if not isinstance(s, set) or not all((isinstance(i, int) for i in s)):
            raise ValueError('All arguments must be sets of integers.')
        original_set.update(s)
    return original_set