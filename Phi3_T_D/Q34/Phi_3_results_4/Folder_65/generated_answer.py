def find_original_set(*args):
    if len(args) != 80:
        raise ValueError('Exactly 80 arguments are required, and each must be a set of integers.')
    original_set = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise ValueError('All arguments must be sets of integers.')
        original_set.update(arg)
    return original_set