def find_original_set(*args):
    if len(args) != 60:
        raise ValueError('Exactly 60 arguments required.')
    original = set()
    for s in args:
        original.update(s)
    return original