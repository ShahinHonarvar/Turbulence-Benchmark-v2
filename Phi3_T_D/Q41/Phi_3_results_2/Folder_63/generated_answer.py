def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    common_elements = set(list1[22:89]) & set(list2[22:89])
    return common_elements