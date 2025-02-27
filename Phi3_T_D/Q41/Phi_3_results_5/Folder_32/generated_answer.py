def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must have the same size')
    common_elements = set([x for i, x in enumerate(list1[20:97 + 1]) if x in list2[20:97 + 1]])
    return common_elements