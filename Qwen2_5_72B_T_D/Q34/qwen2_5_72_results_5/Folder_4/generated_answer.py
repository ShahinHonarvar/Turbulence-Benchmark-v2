def find_original_set(*args):
    if len(args) != 40:
        raise ValueError('Exactly 40 arguments are required')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set