def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    common_elements = set(list1[34:56]) & set(list2[34:56])
    return common_elements