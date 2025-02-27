def find_original_set(*args):
    if len(args) != 48 or len(set(map(len, args))) != len(args):
        raise ValueError('Exactly 48 distinct sets required, each with a unique length')
    result_set = set()
    for arg in args:
        result_set.update(arg)
    return result_set