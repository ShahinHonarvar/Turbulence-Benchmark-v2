def find_original_set(*args):
    if len(args) != 8:
        raise ValueError('Exactly 8 distinct sets are required')
    all_elements = set().union(*args)
    return all_elements