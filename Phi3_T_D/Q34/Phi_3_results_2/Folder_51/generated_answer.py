def find_original_set(*args):
    if len(args) != 28:
        raise ValueError('Exactly 28 arguments expected')
    combined_set = set()
    for arg in args:
        if not isinstance(arg, set):
            arg = set(arg)
        combined_set.update(arg)
    return combined_set