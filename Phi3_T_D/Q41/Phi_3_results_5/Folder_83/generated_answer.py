def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size.')
    return {list1[i] for i in range(90, 201) if list1[i] in list2}