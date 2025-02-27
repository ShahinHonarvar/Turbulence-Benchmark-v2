def identical_elements(list_1, list_2):
    if len(list_1) != len(list_2):
        raise ValueError('Lists must be of the same size.')
    result = set()
    for i in range(31, 73):
        if list_1[i] == list_2[i]:
            result.add(list_1[i])
    return result