def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must have the same length')
    common_elements = set()
    for i in range(209, min(len(list1), 556) + 1):
        if list1[i] in list2 and list2[i] in list1:
            common_elements.add(list1[i])
    return common_elements