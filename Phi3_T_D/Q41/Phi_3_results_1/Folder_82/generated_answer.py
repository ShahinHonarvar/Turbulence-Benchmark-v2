def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('The lists must be the same size.')
    return {list1[i] for i in range(20, min(len(list1), 201)) if list1[i] in list2[i]}