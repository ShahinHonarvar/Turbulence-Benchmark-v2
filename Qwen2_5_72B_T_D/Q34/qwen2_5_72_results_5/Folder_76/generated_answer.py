def find_original_set(*args):
    if len(args) != 247:
        raise ValueError('Exactly 247 arguments required')
    result = set()
    for s in args:
        result.update(s)
    return result