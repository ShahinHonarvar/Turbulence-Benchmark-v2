def find_original_set(*args):
    if len(args) != 99:
        raise ValueError('Exactly 99 arguments must be provided')
    if not all((isinstance(arg, set) and len(arg) == 99 for arg in args)):
        raise ValueError('All arguments must be sets of 99 distinct integers')
    original_set = set().union(*args)
    return original_set