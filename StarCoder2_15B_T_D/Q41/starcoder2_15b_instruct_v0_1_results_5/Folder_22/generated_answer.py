def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    elements = set()
    for i in range(len(list1)):
        if 40 <= i <= 200 and list1[i] in list2[i]:
            elements.add(list1[i])
    return elements