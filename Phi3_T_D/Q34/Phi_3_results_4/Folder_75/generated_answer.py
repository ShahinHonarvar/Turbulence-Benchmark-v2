def find_original_set(*args):
    if not args or len(args) != 15:
        raise ValueError('Exactly 15 arguments are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set):
            raise ValueError('All arguments must be sets.')
        original_set.update(arg)
    return original_set