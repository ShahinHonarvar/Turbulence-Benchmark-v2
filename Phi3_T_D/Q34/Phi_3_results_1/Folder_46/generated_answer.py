def find_original_set(*sets):
    if len(sets) != 828:
        raise ValueError('Exactly 828 sets are required.')
    if not all((isinstance(s, set) for s in sets)):
        raise TypeError('All arguments must be sets of integers.')
    original_set = set().union(*sets)
    return original_set