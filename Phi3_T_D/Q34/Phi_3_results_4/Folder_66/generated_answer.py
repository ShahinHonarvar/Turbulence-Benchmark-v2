def find_original_set(*sets):
    if len(sets) != 25:
        raise ValueError('Exactly 25 sets are required as arguments')
    combined_set = set()
    for s in sets:
        if not isinstance(s, set) or not all((isinstance(i, int) for i in s)):
            raise ValueError('Each argument must be a set of integers')
        combined_set |= s
    return combined_set