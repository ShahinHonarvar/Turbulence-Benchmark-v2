def find_original_set(*args):
    if len(args) != 96:
        raise ValueError('The function requires exactly 96 arguments.')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set