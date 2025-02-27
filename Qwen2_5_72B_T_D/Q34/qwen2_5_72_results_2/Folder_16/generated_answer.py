def find_original_set(*args):
    if len(args) != 321:
        raise ValueError('The function must be called with exactly 321 arguments.')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('All arguments must be sets.')
        result_set.update(arg)
    return result_set