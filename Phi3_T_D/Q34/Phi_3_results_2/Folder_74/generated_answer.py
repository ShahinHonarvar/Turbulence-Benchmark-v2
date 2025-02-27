def find_original_set(*args):
    if len(args) != 96:
        raise ValueError('Exactly 96 arguments are required.')
    result = set()
    for arg in args:
        if not isinstance(arg, set):
            raise TypeError('Each argument must be a set of integers.')
        result.update(arg)
    return result