def find_original_set(*args):
    if len(args) != 64:
        raise ValueError('Exactly 64 arguments are required')
    result = set()
    for arg in args:
        if not isinstance(arg, set) or not all((isinstance(i, int) for i in arg)):
            raise TypeError('All arguments must be sets of integers')
        result.update(arg)
    return result