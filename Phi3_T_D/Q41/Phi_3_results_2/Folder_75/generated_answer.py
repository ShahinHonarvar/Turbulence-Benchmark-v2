def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    overlap = set(list1[56:57]).intersection(set(list2[56:57]))
    return overlap