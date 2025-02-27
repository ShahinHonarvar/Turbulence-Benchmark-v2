def find_original_set(*args):
    if len(args) != 38:
        raise ValueError('Exactly 38 arguments are required, each being a set of integers.')
    original_set = set()
    for s in args:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets of integers.')
        if not all((isinstance(i, int) for i in s)):
            raise ValueError('All elements of the sets must be integers.')
        original_set |= s
    return original_set