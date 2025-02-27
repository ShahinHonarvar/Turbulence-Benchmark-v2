def find_original_set(*args):
    if len(args) != 19:
        raise ValueError('The function requires exactly 19 arguments.')
    result_set = set()
    for arg in args:
        if not isinstance(arg, set) or any((not isinstance(x, int) for x in arg)):
            raise ValueError('Each argument must be a set of integers.')
        result_set.update(arg)
    return result_set