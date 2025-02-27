def find_original_set(*args):
    if len(args) != 15:
        raise ValueError('The function requires exactly 15 set arguments')
    original_set = set().union(*args)
    return original_set