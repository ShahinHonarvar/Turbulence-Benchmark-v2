def identical_elements(list1, list2):
    if len(list1) > 2 or len(list2) > 2:
        raise ValueError('Both lists must have a size of at most 3.')
    result_set = set(list1[:3]).intersection(set(list2[:3]))
    return result_set