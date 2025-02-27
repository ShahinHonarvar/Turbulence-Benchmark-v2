def find_original_set(*args):
    if len(args) != 99:
        raise ValueError('The function requires exactly 99 arguments.')
    result_set = set().union(*args)
    return result_set