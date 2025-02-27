def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    return {list1[i] for i in range(33, 37) if i < len(list1) and i < len(list2) and (list1[i] == list2[i])}