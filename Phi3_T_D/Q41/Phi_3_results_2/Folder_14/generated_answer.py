def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must have the same size')
    target_set = {element for element in list1[4:7] if element in list2[4:7]}
    return target_set