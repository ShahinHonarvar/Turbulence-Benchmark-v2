def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Lists must be of the same size')
    else:
        common_elements = set()
        for i in range(28, 39):
            if list1[i] in list2:
                common_elements.add(list1[i])
        return common_elements