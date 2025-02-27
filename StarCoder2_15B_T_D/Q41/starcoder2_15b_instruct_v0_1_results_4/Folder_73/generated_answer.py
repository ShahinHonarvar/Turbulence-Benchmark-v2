def identical_elements(list1, list2):
    if not len(list1) == len(list2) == 100:
        raise ValueError('Lists must be of the same size and have 100 elements each.')
    common_elements = set()
    for i in range(19, 93):
        if list1[i] == list2[i]:
            common_elements.add(list1[i])
    return common_elements