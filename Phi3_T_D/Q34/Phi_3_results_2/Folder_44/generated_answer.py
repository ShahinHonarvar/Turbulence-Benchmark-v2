def find_original_set(*args):
    if len(args) != 926:
        raise ValueError('Exactly 926 distinct arguments are required')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("All arguments must be of type 'set'")
        original_set.update(arg)
    return original_set