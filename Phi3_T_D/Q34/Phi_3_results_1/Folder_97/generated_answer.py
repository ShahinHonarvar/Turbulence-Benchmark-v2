def find_original_set(*args):
    if len(args) != 194:
        raise ValueError('Exactly 194 arguments required, each a set of integers')
    original_set = set()
    for subset in args:
        if not isinstance(subset, set):
            raise TypeError('All arguments must be sets of integers')
        for num in subset:
            original_set.add(num)
    return sorted(original_set)