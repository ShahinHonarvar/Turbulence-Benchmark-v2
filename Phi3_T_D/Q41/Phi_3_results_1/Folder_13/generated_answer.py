def identical_elements(list1, list2):
    if len(list1) != len(list2):
        raise ValueError('Both lists must be of the same size.')
    overlapping_elements = set(list1[25:88]) & set(list2[25:88])
    return overlapping_elements