def find_original_set(*args):
    r = set()
    for s in args:
        r |= s
    return r