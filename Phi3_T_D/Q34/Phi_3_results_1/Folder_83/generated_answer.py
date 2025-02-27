def find_original_set(*args):
    if len(args) != 64 or any((len(arg) != len(args[0]) for arg in args)):
        raise ValueError('Exactly 64 distinct arguments are required, each being sets of equal length.')
    original_set = set().union(*args)
    return original_set