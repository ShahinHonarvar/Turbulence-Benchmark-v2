def find_original_set(*args):
    result_set = set()
    for single_set in args:
        result_set.update(single_set)
    return result_set