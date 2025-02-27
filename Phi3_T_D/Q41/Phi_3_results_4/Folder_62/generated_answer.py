def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    return set(list1[90:100]) & set(list2[90:100])