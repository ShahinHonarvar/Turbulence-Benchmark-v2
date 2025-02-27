def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('The lists must be of the same size.')
    result = set()
    for i in range(82, 87):
        if list1[i] in list2:
            result.add(list1[i])
    return result