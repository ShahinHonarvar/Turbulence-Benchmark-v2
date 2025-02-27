def find_original_set(*args):
    if len(args) != 162:
        raise ValueError('The function requires exactly 162 distinct set arguments.')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set