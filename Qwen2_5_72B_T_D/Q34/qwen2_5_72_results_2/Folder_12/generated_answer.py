def find_original_set(*args):
    if len(args) != 51:
        raise ValueError('The function requires exactly 51 arguments.')
    result_set = set()
    for arg in args:
        result_set |= arg
    return result_set