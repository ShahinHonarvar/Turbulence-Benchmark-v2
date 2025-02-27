def find_original_set(*args):
    if len(args) != 51:
        raise ValueError('Function requires exactly 51 set arguments')
    original_set = set().union(*args)
    return original_set