def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('The lists must be of the same size.')
    common_elements = {list1[i] for i in range(55, 99) if list1[i] in list2[55:99]}
    return common_elements