def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('The two lists must have the same size.')
    result = set()
    for i in range(31, 73):
        if list1[i] == list2[i]:
            result.add(list1[i])
    return result