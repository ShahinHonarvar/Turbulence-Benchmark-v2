def find_original_set(*args):
    if len(args) != 321:
        raise ValueError('The function requires exactly 321 arguments.')
    result = set()
    for arg in args:
        result.update(arg)
    return result