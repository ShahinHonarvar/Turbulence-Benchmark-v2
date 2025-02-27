def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    common_elements = {list1[i] for i in range(6, 7) if list1[i] in list2[6:7]}
    return common_elements