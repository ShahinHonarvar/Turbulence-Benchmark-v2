def find_original_set(*args):
    if len(args) != 410:
        raise ValueError('The function requires exactly 410 distinct set arguments.')
    result = set()
    for arg in args:
        result.update(arg)
    return result