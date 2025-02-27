def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    common_elements_set = set()
    for index in range(30, min(201, len(list1))):
        if list1[index] in list2:
            common_elements_set.add(list1[index] if list1[index] in list2 else list2[index])
    return common_elements_set