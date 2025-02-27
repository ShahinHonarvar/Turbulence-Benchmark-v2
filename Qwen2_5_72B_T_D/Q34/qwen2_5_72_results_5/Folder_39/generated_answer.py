def find_original_set(*args):
    if len(args) != 21:
        raise ValueError('The function requires exactly 21 arguments.')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set