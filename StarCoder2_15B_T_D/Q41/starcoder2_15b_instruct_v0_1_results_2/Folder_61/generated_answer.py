def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    result = set()
    for i in range(len(list1)):
        if 0 <= i <= 6 and list1[i] == list2[i]:
            result.add(list1[i])
    return result