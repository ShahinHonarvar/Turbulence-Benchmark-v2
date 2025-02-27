def find_original_set(*args):
    if not all((isinstance(arg, set) for arg in args)):
        raise ValueError('All arguments must be sets of integers.')
    if len(args) != 54:
        raise ValueError('Exactly 54 arguments are required.')
    return set.union(*args)