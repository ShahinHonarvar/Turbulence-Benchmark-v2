def find_original_set(*args):
    if len(args) != 56:
        raise ValueError('Must provide exactly 56 arguments')
    result = set()
    for arg in args:
        result.update(arg)
    return result