def find_original_set(*args):
    if len(args) != 410:
        raise ValueError('Expected 410 arguments')
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set