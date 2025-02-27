def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size.')
    result_set = set(list1[50:201] + list2[50:201])
    return {element for element in result_set if element in list1[:50] + list1[201:] and element in list2[:50] + list2[201:]}