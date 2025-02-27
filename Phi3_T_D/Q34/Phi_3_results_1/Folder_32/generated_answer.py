def find_original_set(*args):
    original_set = set().union(*args) if args else set()
    return original_set