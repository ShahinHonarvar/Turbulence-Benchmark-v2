def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size.')
    result_set = set(list1[60:201]) & set(list2[60:201])
    return result_set