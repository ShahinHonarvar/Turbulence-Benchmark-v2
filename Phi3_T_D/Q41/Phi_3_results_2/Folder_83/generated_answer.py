def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    return {val for idx, val in enumerate(list1[90:201]) if val in list2[90:201]}