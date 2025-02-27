def find_original_set(*args):
    if len(args) != 453:
        raise ValueError('Exactly 453 arguments required')
    result = set()
    for arg in args:
        result.update(arg)
    return result