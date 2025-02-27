def find_original_set(*args):
    if len(args) != 24:
        raise ValueError('Function requires exactly 24 arguments.')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set