def find_original_set(*args):
    if len(args) != 849 or any((len(arg) != len(args[0]) for arg in args)):
        raise ValueError('Exactly 849 distinct sets of integers are required, each with the same number of elements.')
    return set.intersection(*args)