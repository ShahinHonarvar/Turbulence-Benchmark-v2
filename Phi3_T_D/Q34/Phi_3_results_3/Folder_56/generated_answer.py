def find_original_set(*args):
    if not all((isinstance(arg, set) and len(arg) <= 63 for arg in args)):
        raise ValueError('All arguments must be sets of integers with up to 63 elements')
    original_set = set().union(*args)
    return original_set