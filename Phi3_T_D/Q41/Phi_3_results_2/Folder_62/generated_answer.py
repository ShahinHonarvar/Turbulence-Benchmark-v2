def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must have the same size.')
    return set(list1[90:99]) & set(list2[90:99])