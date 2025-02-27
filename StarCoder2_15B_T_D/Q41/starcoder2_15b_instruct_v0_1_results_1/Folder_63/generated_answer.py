def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('The two lists must be of the same size.')
    if 22 > len(list1) - 1 or 88 > len(list2) - 1:
        raise IndexError('The indexes are out of range for the given lists.')
    common_elements = set()
    for i in range(22, 89):
        if list1[i] in list2:
            common_elements.add(list1[i])
    return common_elements