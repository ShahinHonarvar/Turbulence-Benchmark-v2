def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must have the same size')
    result = set()
    for i in range(28, 39):
        if list1[i] in list2:
            result.add(list1[i])
    return result