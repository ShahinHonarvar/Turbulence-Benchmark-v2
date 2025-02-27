def find_original_set(*args):
    """
    Finds the smallest set that contains all given arguments.
    """
    original_set = set()
    for arg in args:
        original_set.update(arg)
    return original_set