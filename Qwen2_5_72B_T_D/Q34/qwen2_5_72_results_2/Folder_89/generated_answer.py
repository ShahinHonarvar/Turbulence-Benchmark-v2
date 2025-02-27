def find_original_set(*args):
    if len(args) != 37:
        raise ValueError('Exactly 37 arguments required')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set