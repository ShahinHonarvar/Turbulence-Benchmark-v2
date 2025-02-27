def find_original_set(*args):
    if len(args) != 415:
        raise ValueError('The function requires exactly 415 arguments.')
    result_set = set().union(*args)
    return result_set