def find_original_set(*args):
    if len(args) != 64 or any((len(s) != len(args[0]) for s in args)):
        raise ValueError('Exactly 64 distinct arguments of equal length are expected.')
    original_set = set(args[0])
    for arg in args[1:]:
        original_set.update(arg)
    return original_set