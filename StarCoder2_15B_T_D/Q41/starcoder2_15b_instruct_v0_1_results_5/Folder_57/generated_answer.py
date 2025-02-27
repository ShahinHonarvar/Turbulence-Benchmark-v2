def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    elements_set = set()
    for i in range(len(list1)):
        if list1[i] in list2[i] and 27 <= i <= 55:
            elements_set.add(list1[i])
    return elements_set