def find_original_set(*args):
    if len(args) != 34:
        raise ValueError('Exactly 34 arguments required')
    result = set()
    for s in args:
        result.update(s)
    return result