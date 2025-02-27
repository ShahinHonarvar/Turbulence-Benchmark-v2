def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size')
    elements_at_index_62_63 = {list1[62], list2[62], list1[63], list2[63]}
    return elements_at_index_62_63.intersection(list1).intersection(list2)