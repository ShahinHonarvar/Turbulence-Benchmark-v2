def find_original_set(*args):
    if len(args) != 162:
        raise ValueError('Exactly 162 arguments are required, each representing a set of integers.')
    original_set = set()
    for s in args:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets of integers.')
        original_set.update(s)
    return original_set