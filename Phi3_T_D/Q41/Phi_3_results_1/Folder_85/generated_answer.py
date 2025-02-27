def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size')
    return set(list1[6:9]) & set(list2[6:9])