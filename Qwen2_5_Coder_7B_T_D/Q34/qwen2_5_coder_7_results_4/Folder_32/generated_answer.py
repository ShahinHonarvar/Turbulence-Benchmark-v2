def find_original_set(*sets):
    all_elements = set().union(*sets)
    for size in range(1, len(all_elements) + 1):
        for subset in itertools.combinations(all_elements, size):
            candidate = set(subset)
            if all((candidate.issubset(s) for s in sets)):
                return candidate
    return None