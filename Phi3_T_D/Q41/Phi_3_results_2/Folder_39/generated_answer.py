def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    elements = set()
    for i in range(20, 31):
        if list1[i] in list2:
            elements.add(list1[i])
    return elements