def find_original_set(*args):
    if len(args) != 41:
        raise ValueError('The function must be called with exactly 41 distinct set arguments.')
    result_set = set()
    for s in args:
        result_set.update(s)
    return result_set