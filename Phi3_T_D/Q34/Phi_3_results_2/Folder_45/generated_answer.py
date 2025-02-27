def find_original_set(*args):
    all_elements = set().union(*args)
    original_set = {x for x in all_elements}
    return original_set