def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists should have the same size.')
    result_set = set(list1[22:51]) & set(list2[22:51])
    return result_set