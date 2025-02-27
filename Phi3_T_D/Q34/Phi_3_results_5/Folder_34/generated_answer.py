def find_original_set(*args):
    if len(args) == 0 or len(args) > 95:
        raise ValueError('Function must take exactly 95 arguments')
    original_set = set()
    for s in args:
        if not isinstance(s, set):
            raise TypeError('All arguments must be sets of integers')
        if len(s) != len(set(s)):
            raise ValueError('Set elements must be distinct')
        original_set.update(s)
    return original_set