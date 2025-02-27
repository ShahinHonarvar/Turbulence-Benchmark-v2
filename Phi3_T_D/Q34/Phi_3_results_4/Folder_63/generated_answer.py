def find_original_set(*args):
    if len(args) != 18:
        raise ValueError('Exactly 18 arguments are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets of integers.')
        if not all((isinstance(item, int) for item in arg)):
            raise TypeError('All sets must contain only integers.')
        original_set |= arg
    unique_integers = len(original_set)
    if unique_integers == 18:
        return original_set
    original_set2 = set()
    for i in range(1, unique_integers + 1):
        for subset in combinations(original_set, i):
            if all((any((x in arg for x in subset)) for arg in args)):
                original_set2 = set(subset)
                unique_integers2 = len(original_set2)
                if unique_integers2 < unique_integers:
                    unique_integers = unique_integers2
                    original_set = original_set2
    return original_set