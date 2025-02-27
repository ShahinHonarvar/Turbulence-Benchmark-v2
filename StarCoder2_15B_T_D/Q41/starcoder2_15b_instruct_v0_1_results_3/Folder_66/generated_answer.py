def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of equal size')
    return set(list1[50:55]) & set(list2[50:55])