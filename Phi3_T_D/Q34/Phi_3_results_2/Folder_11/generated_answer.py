def find_original_set(*args):
    if len(args) != 54:
        raise ValueError('Exactly 54 arguments are required.')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError("All arguments must be of type 'set'.")
        result_set.update(arg)
    return result_set