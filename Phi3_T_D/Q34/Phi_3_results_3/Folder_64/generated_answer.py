def find_original_set(*args):
    if not all((isinstance(arg, set) for arg in args)) or len(args) != 7:
        raise ValueError('Arguments must be exactly 7 sets')
    original_set = set().union(*args)
    return original_set