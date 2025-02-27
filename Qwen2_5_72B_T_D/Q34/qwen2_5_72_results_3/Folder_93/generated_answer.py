def find_original_set(*args):
    if len(args) != 90:
        raise ValueError('The function must be called with exactly 90 arguments.')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set