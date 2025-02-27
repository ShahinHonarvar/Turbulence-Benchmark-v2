def find_original_set(*args):
    if len(args) != 47:
        raise ValueError('Exactly 47 arguments are required.')
    common_elements = set.intersection(*args)
    for arg in args:
        common_elements = common_elements.union(arg)
    return common_elements