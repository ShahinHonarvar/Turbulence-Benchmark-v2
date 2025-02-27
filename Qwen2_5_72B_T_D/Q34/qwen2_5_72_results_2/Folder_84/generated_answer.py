def find_original_set(*args):
    if len(args) != 132:
        raise ValueError('The number of arguments must be exactly 132.')
    result = set()
    for arg in args:
        result.update(arg)
    return result