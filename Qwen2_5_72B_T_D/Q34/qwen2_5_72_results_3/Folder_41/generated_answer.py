def find_original_set(*args):
    if len(args) != 20:
        raise ValueError('Function requires exactly 20 arguments.')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set