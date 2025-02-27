def find_original_set(*args):
    if len(args) != 68 or len(set(args)) != 68:
        raise ValueError('Exactly 68 distinct arguments expected')
    original_set = set()
    for s in args:
        if not isinstance(s, set):
            raise ValueError(f'Argument {s} is not a set')
        original_set.update(s)
    return original_set