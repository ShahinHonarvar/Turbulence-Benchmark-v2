def find_original_set(*args):
    if not args or len(args) != 56:
        raise ValueError('Exactly 56 distinct arguments expected')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets of integers')
        result.update(arg)
    return result