def find_original_set(*args):
    if len(args) != 24:
        raise ValueError('Must provide exactly 24 set arguments')
    result_set = args[0]
    for s in args[1:]:
        result_set.update(s)
    return result_set