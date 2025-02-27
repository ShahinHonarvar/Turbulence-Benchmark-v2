def find_original_set(*args):
    if len(args) != 42:
        raise ValueError('Function requires exactly 42 arguments.')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set