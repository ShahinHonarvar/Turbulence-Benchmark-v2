def find_original_set(*args):
    if len(args) != 415:
        raise ValueError('The function must receive exactly 415 distinct arguments.')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set