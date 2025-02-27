def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must have the same size.')
    return {list1[i] for i in range(6, 7) if i < len(list1) and list1[i] in list2}