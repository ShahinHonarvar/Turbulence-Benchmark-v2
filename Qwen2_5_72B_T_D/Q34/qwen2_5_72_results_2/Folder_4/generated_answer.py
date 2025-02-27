def find_original_set(*args):
    if len(args) != 40:
        raise ValueError('The function requires exactly 40 arguments.')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set