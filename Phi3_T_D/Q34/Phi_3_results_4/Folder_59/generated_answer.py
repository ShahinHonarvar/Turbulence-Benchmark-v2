def find_original_set(*args):
    original_set = set()
    for s in args:
        if type(s) is not set:
            raise TypeError('All arguments must be sets.')
        if len(s) != len(set(s)):
            raise ValueError('All sets must contain distinct integers.')
        original_set.update(s)
    return original_set