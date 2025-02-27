def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same length')
    return set(list1[22:89]) & set(list2[22:89])