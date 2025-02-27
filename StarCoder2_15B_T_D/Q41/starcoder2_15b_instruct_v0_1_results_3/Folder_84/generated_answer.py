def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    common_elements = set()
    for index in range(43, 87):
        if list1[index] == list2[index]:
            common_elements.add(list1[index])
    return common_elements