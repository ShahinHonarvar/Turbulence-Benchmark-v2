def find_original_set(*args):
    if len(args) != 24:
        raise ValueError('Exactly 24 arguments are required.')
    result_set = set.union(*args)
    return result_set