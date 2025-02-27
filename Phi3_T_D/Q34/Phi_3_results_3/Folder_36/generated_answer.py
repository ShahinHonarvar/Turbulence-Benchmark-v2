def find_original_set(*args):
    if len(args) != 714:
        raise ValueError('Exactly 714 arguments must be provided')
    original_set = set()
    for s in args:
        if not isinstance(s, set):
            raise ValueError('All arguments must be sets of integers')
        original_set |= s
    return original_set