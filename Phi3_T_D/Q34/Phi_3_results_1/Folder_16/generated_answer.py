def find_original_set(*args):
    if len(args) != 321:
        raise ValueError('Exactly 321 arguments are required.')
    all_elements = set().union(*args)
    original_set = set(sorted(all_elements))
    return original_set