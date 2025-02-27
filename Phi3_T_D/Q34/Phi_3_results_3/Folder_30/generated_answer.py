def find_original_set(*args):
    if len(args) != 78:
        raise ValueError('Exactly 78 arguments are required.')
    if not all((isinstance(arg, set) for arg in args)):
        raise TypeError('All arguments must be of type set.')
    original_set = set().union(*args)
    return original_set