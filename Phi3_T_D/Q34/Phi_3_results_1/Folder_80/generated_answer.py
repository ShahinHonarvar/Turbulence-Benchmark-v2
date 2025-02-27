def find_original_set(*args):
    if len(args) != 453:
        raise ValueError('Exactly 453 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be sets.')
    original_set = set()
    for subset in args:
        original_set.update(subset)
    return original_set