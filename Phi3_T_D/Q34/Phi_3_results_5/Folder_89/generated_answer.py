def find_original_set(*args):
    if not args or len(args) != 37:
        raise ValueError('Exactly 37 arguments are required, each being a set of integers.')
    result = set().union(*args)
    for s in args:
        if not s.issubset(result):
            result.update(s)
    return result