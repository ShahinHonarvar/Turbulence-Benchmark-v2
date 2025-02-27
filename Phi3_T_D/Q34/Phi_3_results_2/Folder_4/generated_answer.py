def find_original_set(*args):
    if not 40 <= len(args) <= 40:
        raise ValueError('Function should be called with exactly 40 arguments.')
    result_set = set()
    for arg in args:
        if not (isinstance(arg, set) and len(arg) == 40):
            raise ValueError('Each argument should be a set of 40 distinct integers.')
        result_set.update(arg)
    return result_set