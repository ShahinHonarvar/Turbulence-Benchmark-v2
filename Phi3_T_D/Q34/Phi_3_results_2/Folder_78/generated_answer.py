def find_original_set(*sets_of_integers):
    if len(sets_of_integers) != 48:
        raise ValueError('Exactly 48 sets of integers are required.')
    original_set = set()
    for subset in sets_of_integers:
        if not subset.issubset(original_set):
            original_set = original_set.union(subset)
    return original_set