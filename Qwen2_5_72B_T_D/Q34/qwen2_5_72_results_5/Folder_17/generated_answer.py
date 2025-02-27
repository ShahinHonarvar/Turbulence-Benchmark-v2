def find_original_set(*args):
    if len(args) != 478:
        raise ValueError('The function must be called with exactly 478 distinct set arguments.')
    result = set()
    for s in args:
        result.update(s)
    return result