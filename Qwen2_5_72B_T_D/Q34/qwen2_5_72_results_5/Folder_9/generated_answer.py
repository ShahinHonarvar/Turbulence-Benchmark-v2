def find_original_set(*args):
    if len(args) != 73:
        raise ValueError('The function requires exactly 73 distinct set arguments.')
    result_set = set().union(*args)
    return result_set