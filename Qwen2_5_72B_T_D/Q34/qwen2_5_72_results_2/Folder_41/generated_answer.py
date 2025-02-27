def find_original_set(*args):
    if len(args) != 20:
        raise ValueError('Must provide exactly 20 distinct sets')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set