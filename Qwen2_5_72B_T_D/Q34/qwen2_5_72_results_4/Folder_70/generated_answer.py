def find_original_set(*args):
    if len(args) != 312:
        raise ValueError('The function requires exactly 312 distinct sets as arguments.')
    result_set = set().union(*args)
    return result_set