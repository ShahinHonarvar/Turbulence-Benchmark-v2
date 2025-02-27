def find_original_set(*args):
    if len(args) != 28:
        raise ValueError('The function requires exactly 28 distinct set arguments.')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set