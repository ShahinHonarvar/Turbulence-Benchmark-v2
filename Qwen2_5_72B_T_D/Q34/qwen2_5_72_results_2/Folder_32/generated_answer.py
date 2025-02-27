def find_original_set(*args):
    if len(args) != 459:
        raise ValueError('The function must be called with exactly 459 distinct set arguments.')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set