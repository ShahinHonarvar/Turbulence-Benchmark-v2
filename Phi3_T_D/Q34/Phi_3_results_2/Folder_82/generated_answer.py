def find_original_set(*args):
    if len(args) != 47:
        raise ValueError('Exactly 47 arguments are required.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(n, int) for n in arg)):
            raise ValueError('Each argument must be a set of integers.')
        original_set.update(arg)
    return original_set