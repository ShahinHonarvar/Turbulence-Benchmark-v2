def find_original_set(*args):
    if len(args) != 478:
        raise ValueError('The function requires exactly 478 arguments.')
    return set().union(*args)