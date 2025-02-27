def find_original_set(*args):
    if not args or len(args) != 48:
        return None
    original_set = set().union(*args)
    return original_set