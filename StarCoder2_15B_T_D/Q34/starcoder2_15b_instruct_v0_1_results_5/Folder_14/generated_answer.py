def find_original_set(*args):
    master_set = set()
    for arg in args:
        master_set |= arg
    return master_set