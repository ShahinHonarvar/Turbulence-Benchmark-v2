def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    identical_elements_set = set()
    for i in range(0, 6):
        if list1[i] == list2[i]:
            identical_elements_set.add(list1[i])
    return identical_elements_set