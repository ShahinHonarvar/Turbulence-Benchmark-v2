def identical_elements(list_1, list_2):
    if len(list_1) != len(list_2):
        raise ValueError('Lists must be of the same size')
    elements = set()
    for i in range(5):
        if list_1[i] == list_2[i]:
            elements.add(list_1[i])
    return elements