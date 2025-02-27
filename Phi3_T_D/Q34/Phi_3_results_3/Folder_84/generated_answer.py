def find_original_set(*args):
    if not args or len(args) != 132:
        raise ValueError('Exactly 132 arguments required.')
    result = set()
    for arg in args:
        result.update(arg)
    return result